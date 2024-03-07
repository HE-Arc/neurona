import string
import random
import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from neuronaApp.models import Challenges
from neuronaApp.serializers.passkey_serializer import ChallengeSerializer

CHALLENGE_CHARACTERS = string.ascii_lowercase + string.ascii_uppercase + string.digits
CHALLENGE_SIZE = 64
CHALLENGE_EXPIRATION_MS = 300000 # 5 minutes, see https://w3c.github.io/webauthn/#sctn-timeout-recommended-range


def get_random_challenge():
    return "".join(random.choices(CHALLENGE_CHARACTERS, k=CHALLENGE_SIZE))


class PasskeyChallengeView(viewsets.ModelViewSet):

    queryset = Challenges.objects.all()
    serializer_class = ChallengeSerializer

    def create(self, request, **kwargs):
        challenge = Challenges()
        challenge.challenge = get_random_challenge()
        challenge.expires_at = datetime.datetime.now() + datetime.timedelta(milliseconds=CHALLENGE_EXPIRATION_MS)
        challenge.save()

        serializer = self.get_serializer(challenge)
        return Response(serializer.data)


