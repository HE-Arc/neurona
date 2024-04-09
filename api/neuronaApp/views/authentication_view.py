from django.conf import settings
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from webauthn import options_to_json
from webauthn.helpers.exceptions import InvalidRegistrationResponse, InvalidAuthenticationResponse

from neuronaApp.models import Challenges, User, PublicKeys, ApiKeys
from neuronaApp.serializers.authentication_serializer import ChallengeSerializer, ChallengeIdSerializer, \
    UsernameSerializer, \
    EmailSerializer, UsernameOrEmailSerializer, ApiKeySerializer, DisplayNameSerializer

import webauthn
import logging

from neuronaApp.token_authentication import TokenAuthentication

logger = logging.getLogger('django')


class PasskeyChallengeView(viewsets.ViewSet):
    """
    This view is responsible for generating a challenge for the user to register a new public key.
    It also provides the options for the registration.
    """

    @action(detail=False, methods=["post"])
    def register(self, request, **kwargs):
        username_serializer = UsernameSerializer(data=request.data)
        display_name_serializer = DisplayNameSerializer(data=request.data)

        if not username_serializer.is_valid():
            return Response({
                "error": username_serializer.errors,
                "message": username_serializer.get_error_message()
            }, status=400)

        if not display_name_serializer.is_valid():
            return Response({
                "error": display_name_serializer.errors,
                "message": display_name_serializer.get_error_message()
            }, status=400)

        options = webauthn.generate_registration_options(
            rp_name="Neurona",
            rp_id=getattr(settings, "PASSKEY_RP_ID", "localhost"),
            user_name=username_serializer.validated_data["username"],
        )

        challenge = Challenges().generate_and_get(options.challenge)

        challenge_serializer = ChallengeSerializer(challenge)
        response = {
            "options": options_to_json(options),
            "id": challenge_serializer.data["id"],
        }

        return Response(response, status=201)

    @action(detail=False, methods=["post"])
    def login(self, request, **kwargs):
        username_or_email_serializer = UsernameOrEmailSerializer(data=request.data)

        if not username_or_email_serializer.is_valid():
            return Response({
                "error": username_or_email_serializer.errors,
                "message": username_or_email_serializer.get_error_message()
            }, status=400)

        options = webauthn.generate_authentication_options(
            rp_id=getattr(settings, "PASSKEY_RP_ID", "localhost"),
        )

        challenge = Challenges().generate_and_get(options.challenge)

        challenge_serializer = ChallengeSerializer(challenge)
        response = {
            "options": options_to_json(options),
            "id": challenge_serializer.data["id"],
        }

        return Response(response, status=201)


class RegisterView(APIView):
    """
    This view is responsible for registering a new user with a public key.
    It verifies whether the registration response of the browser is valid and then saves the public key
    and the user in the database.
    """

    def post(self, request, **kwargs):

        # get the credentials and the registration data from the request as a dictionary
        credentials = request.data.get("credentials", {})
        registration_data = request.data.get("data", {})

        username_serializer = UsernameSerializer(data=registration_data)
        challenge_id_serializer = ChallengeIdSerializer(data=registration_data)
        display_name_serializer = DisplayNameSerializer(data=registration_data)

        # if the data is not valid, return the errors
        if not username_serializer.is_valid():
            return Response({
                "error": username_serializer.errors,
                "message": username_serializer.get_error_message()
            }, status=400)

        if not display_name_serializer.is_valid():
            return Response({
                "error": display_name_serializer.errors,
                "message": display_name_serializer.get_error_message()
            }, status=400)

        if not challenge_id_serializer.is_valid():
            return Response({
                "error": challenge_id_serializer.errors,
                "message": challenge_id_serializer.get_error_message()
            }, status=400)

        # get the challenge from the database by the provided id
        challenge_id = challenge_id_serializer.validated_data["challenge_id"]
        challenge = Challenges.objects.get(id=challenge_id)

        # get the challenge data and delete the challenge from the database (it is only valid once)
        challenge_data = challenge.challenge
        challenge.delete()

        # verify the registration response
        try:
            registration_verification = webauthn.verify_registration_response(
                credential=credentials,
                expected_challenge=challenge_data.tobytes(),
                expected_origin=request.headers["Origin"],
                expected_rp_id=getattr(settings, "PASSKEY_RP_ID", "localhost"),
            )
        except InvalidRegistrationResponse as exception:
            logger.error(f"registration_verification: {exception}")
            return Response({"message": "invalid registration response"}, status=400)

        # if the registration response is valid, save the user and the public key in the database
        username = username_serializer.validated_data["username"]
        display_name = display_name_serializer.validated_data["display_name"]

        User(username=username, display_name=display_name).save()
        user = User.objects.get(username=username)

        PublicKeys(
            user=user,
            key=registration_verification.credential_public_key,
            credential_id=registration_verification.credential_id
        ).save()

        api_key = ApiKeys(user=user).generate_and_get()
        api_key_serializer = ApiKeySerializer(api_key)

        return Response({"status": "ok", "token": api_key_serializer.data}, status=201)


class LoginView(APIView):
    """
    The view is responsible for authenticating the user for the login process.
    """

    def post(self, request, **kwargs):
        credentials = request.data.get("credentials", {})
        data = request.data.get("data", {})

        user_serializer = UsernameOrEmailSerializer(data=data)
        challenge_id_serializer = ChallengeIdSerializer(data=data)

        if not user_serializer.is_valid():
            return Response({
                "error": user_serializer.errors,
                "message": user_serializer.get_error_message()
            }, status=400)

        user = user_serializer.get_user()
        logger.info(f"found user = {user.display_name} @ {user.username}")

        if not challenge_id_serializer.is_valid():
            return Response({
                "error": challenge_id_serializer.errors,
                "message": challenge_id_serializer.get_error_message()
            }, status=400)

        # get the challenge from the database by the provided id
        challenge_id = challenge_id_serializer.validated_data["challenge_id"]
        challenge = Challenges.objects.get(id=challenge_id)

        # get the challenge data and delete the challenge from the database (it is only valid once)
        challenge_data = challenge.challenge
        challenge.delete()

        key = PublicKeys.objects.get(user=user)

        try:
            authentication_verification = webauthn.verify_authentication_response(
                credential=credentials,
                expected_challenge=challenge_data.tobytes(),
                expected_origin=request.headers["Origin"],
                expected_rp_id=getattr(settings, "PASSKEY_RP_ID", "localhost"),
                credential_public_key=key.key,
                credential_current_sign_count=0
            )
            api_key = ApiKeys(user=user).generate_and_get()
            api_key_serializer = ApiKeySerializer(api_key)

            return Response({"status": "ok", "token": api_key_serializer.data}, status=200)

        except InvalidAuthenticationResponse as e:
            logger.error(f"authentication_verification: {e}")
            return Response({"message": "Login failed. Please try again."}, status=400)


class LogoutView(APIView):
    """
    This view is responsible for logging out the user.
    """
    authentication_classes = (TokenAuthentication,)

    def post(self, request, **kwargs):
        user = request.user
        api_key = request.auth
        api_key.delete()

        return Response({"status": "ok"}, status=200)
