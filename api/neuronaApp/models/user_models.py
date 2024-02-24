from django.db import models


class Challenges(models.Model):
    challenge = models.CharField(max_length=100)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    display_name = models.CharField(max_length=100)
    passkey_user_id = models.CharField(max_length=100)
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
    key = models.CharField(max_length=5000)
    credential_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ApiKeys(models.Model):
    user = models.ForeignKey(User, related_name='api_keys', on_delete=models.CASCADE)
    key = models.CharField(max_length=256)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)