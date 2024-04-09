import urllib.parse

from rest_framework import serializers

from neuronaApp.models import User

DEFAULT_AVATAR_BASE_URL = "https://avatar.iran.liara.run/username?username="

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "display_name",
            "image_url",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data["image_url"] is None:
            display_name_encoded = urllib.parse.quote_plus(data["display_name"])
            data["image_url"] = DEFAULT_AVATAR_BASE_URL + display_name_encoded
        return data