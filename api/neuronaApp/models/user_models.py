import random

from django.db import models
from django.utils import timezone


class Challenges(models.Model):
    # constants
    DEFAULT_VALIDITY_MS = 300000
    DEFAULT_CHALLENGE_LENGTH = 64

    # fields
    challenge = models.BinaryField()
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # methods
    def has_expired(self):
        return self.expires_at < timezone.now()

    def _get_random_challenge(self):
        return bytes([random.randint(0, 255) for _ in range(self.DEFAULT_CHALLENGE_LENGTH)])

    def _get_expiration_time(self):
        return timezone.now() + timezone.timedelta(milliseconds=self.DEFAULT_VALIDITY_MS)

    def generate_and_get(self, challenge):
        self.challenge = challenge
        self.expires_at = self._get_expiration_time()
        self.save()
        return self


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    display_name = models.CharField(max_length=100, blank=True)
    about = models.TextField(max_length=2000, blank=True)
    image_url = models.URLField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RecoveryCodes(models.Model):
    user = models.ForeignKey(User, related_name='recovery_codes', on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PublicKeys(models.Model):
    user = models.ForeignKey(User, related_name='public_keys', on_delete=models.CASCADE)
    key = models.BinaryField()
    credential_id = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class ApiKeys(models.Model):
    user = models.ForeignKey(User, related_name='api_keys', on_delete=models.CASCADE)
    key = models.CharField(max_length=256)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)