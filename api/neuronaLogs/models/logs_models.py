from django.db import models
from enum import Enum


class Privacy(Enum):
    PUBLIC = "public"
    PROTECTED = "protected"
    RESTRICTED = "restricted"
    PRIVATE = "private"


class UserAction(Enum):
    CREATED = "created"
    DELETED = "deleted"
    CHANGED_EMAIL = "changed_email"
    CHANGED_DISPLAY_NAME = "changed_display_name"
    CHANGED_USERNAME = "changed_username"
    CHANGED_ABOUT = "changed_about"
    CHANGED_IMAGE = "changed_image"


class UserLogs(models.Model):
    user_id = models.IntegerField(null=True)
    display_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    about = models.TextField(max_length=2000, blank=True)
    image_url = models.URLField(max_length=200, null=True)
    action = models.CharField(choices=[(tag, tag.value) for tag in UserAction], max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'neuronaLogs'


class PostAction(Enum):
    CREATED = "created"
    DELETED = "deleted"
    ARCHIVED = "archived"


class PostLogs(models.Model):
    post_id = models.IntegerField(null=True)
    user_id = models.IntegerField()
    admin_id = models.IntegerField(null=True)
    content = models.TextField(max_length=1000)
    action = models.CharField(choices=[(tag, tag.value) for tag in PostAction], max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'neuronaLogs'


class PostImagesLogs(models.Model):
    post_id = models.IntegerField()
    image_url = models.URLField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'neuronaLogs'


class VoteAction(Enum):
    UPVOTED = "upvoted"
    DOWNVOTED = "downvoted"
    CANCELLED_UPVOTE = "cancelled_upvote"
    CANCELLED_DOWNVOTE = "cancelled_downvote"


class PostVoteLogs(models.Model):
    user_id = models.IntegerField()
    post_id = models.IntegerField()
    action = models.CharField(choices=[(tag, tag.value) for tag in VoteAction], max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'neuronaLogs'


class CommentAction(Enum):
    CREATED = "created"
    DELETED = "deleted"


class CommentLogs(models.Model):
    comment_id = models.IntegerField(null=True)
    user_id = models.IntegerField()
    post_id = models.IntegerField()
    content = models.TextField(max_length=1000)
    action = models.CharField(choices=[(tag, tag.value) for tag in CommentAction], max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'neuronaLogs'


class CommentImagesLogs(models.Model):
    comment_id = models.IntegerField()
    image_url = models.URLField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'neuronaLogs'


class CommentVoteLogs(models.Model):
    user_id = models.IntegerField()
    comment_id = models.IntegerField()
    action = models.CharField(choices=[(tag, tag.value) for tag in VoteAction], max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'neuronaLogs'


class SpaceAction(Enum):
    CREATED = "created"
    DELETED = "deleted"
    CHANGED_NAME = "changed_name"
    CHANGED_ABOUT = "changed_about"
    CHANGED_IMAGE = "changed_image"
    CHANGED_PRIVACY = "changed_privacy"


class SpaceLogs(models.Model):
    space_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=2000, blank=True)
    image_url = models.URLField(max_length=200, null=True)
    privacy = models.CharField(choices=[(tag, tag.value) for tag in Privacy], max_length=100)
    action = models.CharField(choices=[(tag, tag.value) for tag in SpaceAction], max_length=100)
    admin_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'neuronaLogs'


class SpaceMemberAction(Enum):
    JOINED = "joined"
    LEFT = "left"
    KICKED = "kicked"
    INVITED = "invited"


class SpaceMemberLogs(models.Model):
    user_id = models.IntegerField()
    space_id = models.IntegerField()
    admin_id = models.IntegerField()
    action = models.CharField(choices=[(tag, tag.value) for tag in SpaceMemberAction], max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'neuronaLogs'


class SpaceAdminAction(Enum):
    ADDED = "added"
    REMOVED = "removed"
    LEFT = "left"


class SpaceAdminLogs(models.Model):
    user_id = models.IntegerField()
    space_id = models.IntegerField()
    admin_id = models.IntegerField()
    action = models.CharField(choices=[(tag, tag.value) for tag in SpaceAdminAction], max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'neuronaLogs'


class SpaceAccessRequestAction(Enum):
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    CANCELLED = "cancelled"
    SENT = "sent"


class SpaceAccessRequestLogs(models.Model):
    user_id = models.IntegerField()
    space_id = models.IntegerField()
    admin_id = models.IntegerField()
    action = models.CharField(choices=[(tag, tag.value) for tag in SpaceAccessRequestAction], max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'neuronaLogs'


class TagAction(Enum):
    CREATED = "created"
    DELETED = "deleted"
    CHANGED_NAME = "changed_name"


class TagLogs(models.Model):
    tag_id = models.IntegerField(null=True)
    space_id = models.IntegerField()
    admin_id = models.IntegerField()
    name = models.CharField(max_length=100)
    action = models.CharField(choices=[(tag, tag.value) for tag in TagAction], max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'neuronaLogs'


class LoginAction(Enum):
    LOGGED_IN = "logged_in"
    LOGGED_IN_WITH_RECOVERY_CODE = "logged_in_with_recovery_code"
    LOGGED_OUT = "logged_out"
    FAILED_LOGIN = "failed_login"


class LoginLogs(models.Model):
    user_id = models.IntegerField()
    action = models.CharField(choices=[(tag, tag.value) for tag in LoginAction], max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'neuronaLogs'
