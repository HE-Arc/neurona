from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from neuronaApp.serializers import UsernameSerializer, EmailSerializer


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
