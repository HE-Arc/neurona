from rest_framework import serializers

from neuronaApp.models import Challenges, User, ApiKeys
import re

USERNAME_MIN_LENGTH = 3
USERNAME_MAX_LENGTH = 15

USERNAME_REGEX = r"^[a-zA-Z][a-zA-Z0-9_]{" + str(USERNAME_MIN_LENGTH) + r"," + str(USERNAME_MAX_LENGTH) + r"}$"
EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Challenges
        fields = [
            "id",
            "challenge",
        ]


class UsernameSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)

    def validate_username(self, value):
        if len(value) < USERNAME_MIN_LENGTH:
            raise serializers.ValidationError(f"Username must be at least {USERNAME_MIN_LENGTH} characters long")

        if len(value) > USERNAME_MAX_LENGTH:
            raise serializers.ValidationError(f"Username must be at most {USERNAME_MAX_LENGTH} characters long")

        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already taken")

        if not re.match(USERNAME_REGEX, value):
            raise serializers.ValidationError("Username must start with a letter and contain only letters, numbers "
                                              "and underscores")

        return value

    def get_error_message(self):
        return self.errors["username"][0]

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already taken")

        if not re.match(EMAIL_REGEX, value):
            raise serializers.ValidationError("Invalid email address")

        return value

    def get_error_message(self):
        return self.errors["email"][0]


class UsernameOrEmailSerializer(serializers.Serializer):
    username_or_email = serializers.CharField(max_length=100)

    def validate_username_or_email(self, value):
        if User.objects.filter(username=value).exists() or User.objects.filter(email=value).exists():
            return value
        raise serializers.ValidationError("Username or email not found")

    def _is_username(self, value):
        return re.match(USERNAME_REGEX, value)

    def get_user(self):
        username_or_email = self.validated_data["username_or_email"]

        if self._is_username(username_or_email):
            return User.objects.get(username=username_or_email)
        return User.objects.get(email=username_or_email)

    def get_error_message(self):
        return self.errors["username_or_email"][0]


class ChallengeIdSerializer(serializers.Serializer):
    challenge_id = serializers.IntegerField()

    def validate_challenge_id(self, value):
        if not Challenges.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid challenge id")

        if Challenges.objects.get(id=value).has_expired():
            raise serializers.ValidationError("Challenge has expired")

        return value

    def get_error_message(self):
        return self.errors["challenge_id"][0]


class ApiKeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiKeys
        fields = [
            "key",
            "expires_at"
            ]