from rest_framework import serializers

from neuronaApp.models import Challenges


class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Challenges
        fields = [
            "id",
            "challenge",
        ]
        