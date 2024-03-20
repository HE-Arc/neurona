from rest_framework import serializers

from neuronaApp.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "display_name",
            "email",
            "image_url",
        ]