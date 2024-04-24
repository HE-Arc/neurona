from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from neuronaApp.models import User
from neuronaApp.serializers import UsernameSerializer, EmailSerializer, UserSerializer, DisplayNameSerializer
from neuronaApp.serializers.users_serializer import BiographySerializer
from neuronaApp.token_authentication import TokenAuthentication


from neuronaApp.views.authentication_view import logger

class Validity(viewsets.ViewSet):
    @action(detail=False, methods=["GET"])
    def username(self, request, *args, **kwargs):
        username = request.query_params.get("username", "")
        serializer = UsernameSerializer(data={"username": username})

        if not serializer.is_valid():
            return Response({"message": serializer.get_error_message()}, status=400)

        return Response(status=200)

    @action(detail=False, methods=["GET"])
    def email(self, request, *args, **kwargs):
        email = request.query_params.get("email", "")
        serializer = EmailSerializer(data={"email": email})

        if not serializer.is_valid():
            return Response({"message": serializer.get_error_message()}, status=400)

        return Response(status=200)

class Profile(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)

    def list(self, request, *args, **kwargs):
        user = request.user
        return Response(UserSerializer(user).data)

    @action(detail=False, methods=['get'], url_path='(?P<username>[^/.]+)')
    def get_profile(self, request, username=None):
        user = User.objects.filter(username=username)

        if not user.exists():
            return Response({"message": "User not found"}, status=404)

        return Response(UserSerializer(user[0]).data)

    @action(detail=False, methods=['delete'])
    def delete(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        return Response(status=204)

    @action(detail=False, methods=["PUT"])
    def username(self, request, *args, **kwargs):
        user = request.user
        serializer = UsernameSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({"message": serializer.get_error_message()}, status=400)

        user.username = serializer.validated_data["username"]
        user.save()

        return Response(status=200)

    @action(detail=False, methods=["PUT"])
    def display_name(self, request, *args, **kwargs):
        user = request.user
        serializer = DisplayNameSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({"message": serializer.get_error_message()}, status=400)

        user.display_name = serializer.validated_data["display_name"]
        user.save()

        return Response(status=200)

    @action(detail=False, methods=["PUT"])
    def about(self, request, *args, **kwargs):
        user = request.user
        serializer = BiographySerializer(data=request.data)

        if not serializer.is_valid():
            return Response({"message": serializer.get_error_message()}, status=400)

        user.about = serializer.validated_data["about"]
        user.save()

        return Response(status=200)