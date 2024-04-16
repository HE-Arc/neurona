import urllib.parse

from rest_framework import serializers

from neuronaApp.models import User

DEFAULT_AVATAR_BASE_URL = "https://avatar.iran.liara.run/username?username="
BIOGRAPHY_MAX_LENGTH = 200


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "display_name",
            "image_url",
            "about",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data["image_url"] is None:
            display_name_encoded = urllib.parse.quote_plus(data["display_name"])
            data["image_url"] = DEFAULT_AVATAR_BASE_URL + display_name_encoded
        return data


class BiographySerializer(serializers.Serializer):
    about = serializers.CharField(max_length=200)

    def validate_about(self, value):
        if len(value) > BIOGRAPHY_MAX_LENGTH:
            raise serializers.ValidationError(f"Biography must be at most {BIOGRAPHY_MAX_LENGTH} characters long")
        return value

    def get_error_message(self):
        return self.errors["about"][0]
