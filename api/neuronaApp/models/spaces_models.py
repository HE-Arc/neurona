from django.db import models
from enum import Enum


class Privacy(Enum):
    PUBLIC = "public"
    PROTECTED = "protected"
    RESTRICTED = "restricted"
    PRIVATE = "private"


class Spaces(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=2000, blank=True)
    image_url = models.URLField(max_length=200, null=True)
    privacy = models.CharField(choices=[(tag, tag.value) for tag in Privacy], max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SpacesMembers(models.Model):
    user = models.ForeignKey('User', related_name='spaces', on_delete=models.CASCADE)
    space = models.ForeignKey(Spaces, related_name='members', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SpacesAdmins(models.Model):
    user = models.ForeignKey('User', related_name='admin_of', on_delete=models.CASCADE)
    space = models.ForeignKey(Spaces, related_name='admins', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SpacesAccessRequests(models.Model):
    user = models.ForeignKey('User', related_name='access_requests', on_delete=models.CASCADE)
    space = models.ForeignKey(Spaces, related_name='access_requests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SpacesInvitations(models.Model):
    user = models.ForeignKey('User', related_name='invitations', on_delete=models.CASCADE)
    space = models.ForeignKey(Spaces, related_name='invitations', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tags(models.Model):
    name = models.CharField(max_length=100)
    space = models.ForeignKey(Spaces, related_name='tags', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)