from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from neuronaApp.models.user_models import *
from neuronaApp.models.posts_models import *
from neuronaApp.models.spaces_models import *
from .logs_models import *


def save_user_log(instance, action):
    UserLogs(
        user_id=instance.pk,
        display_name=instance.display_name,
        username=instance.username,
        about=instance.about,
        image_url=instance.image_url,
        action=action
    ).save()


@receiver(pre_save, sender=User)
def user_changes(sender, instance, **kwargs):
    """
    This method is invoked before saving a User instance.
    It checks which fields have been modified and logs the changes.
    """
    if instance.pk:
        original = sender.objects.get(pk=instance.pk)

        if original.display_name != instance.display_name:
            save_user_log(instance, UserAction.CHANGED_DISPLAY_NAME)

        if original.username != instance.username:
            save_user_log(instance, UserAction.CHANGED_USERNAME)

        if original.about != instance.about:
            save_user_log(instance, UserAction.CHANGED_ABOUT)

        if original.image_url != instance.image_url:
            save_user_log(instance, UserAction.CHANGED_IMAGE)

    else:
        save_user_log(instance, UserAction.CREATED)


def save_post_log(instance: Posts, action, admin_id=None):
    PostLogs(
        post_id=instance.pk,
        user_id=instance.user_id,
        admin_id=admin_id,
        content=instance.content,
        action=action
    ).save()


@receiver(pre_save, sender=Posts)
def post_created_or_archived(sender, instance: Posts, **kwargs):
    """
    """
    if instance.pk:
        original = sender.objects.get(pk=instance.pk)

        if original.is_archived != instance.is_archived:
            save_post_log(instance, PostAction.ARCHIVED)

    else:
        save_post_log(instance, PostAction.CREATED)


@receiver(pre_delete, sender=Posts)
def post_deleted(sender, instance, **kwargs):
    save_post_log(instance, PostAction.DELETED)


@receiver(pre_save, sender=PostsImages)
def post_image_added(sender, instance, **kwargs):
    """
    """
    PostImagesLogs(
        post_id=instance.post_id,
        image_url=instance.image_url
    ).save()


def save_post_vote_log(instance: Votes, action):
    PostVoteLogs(
        post_id=instance.post_id,
        user_id=instance.user_id,
        action=action
    ).save()


@receiver(pre_save, sender=Votes)
def post_vote_changes(sender, instance: Votes, **kwargs):
    action = VoteAction.UPVOTED if instance.is_upvote else VoteAction.DOWNVOTED
    save_post_vote_log(instance, action)


@receiver(pre_delete, sender=Votes)
def post_vote_deleted(sender, instance: Votes, **kwargs):
    action = VoteAction.CANCELLED_UPVOTE if instance.is_upvote else VoteAction.CANCELLED_DOWNVOTE
    save_post_vote_log(instance, action)


def save_comment_log(instance: Comments, action: CommentAction):
    CommentLogs(
        comment_id=instance.pk,
        user_id=instance.user_id,
        post_id=instance.post_id,
        content=instance.content,
        action=action
    ).save()


@receiver(pre_save, sender=Comments)
def comment_created(sender, instance: Comments, **kwargs):
    save_comment_log(instance, CommentAction.CREATED)


@receiver(pre_delete, sender=Comments)
def comment_deleted(sender, instance: Comments, **kwargs):
    save_comment_log(instance, CommentAction.DELETED)


def save_comment_vote_logs(instance: CommentsVotes, action: VoteAction):
    CommentVoteLogs(
        comment_id=instance.comment_id,
        user_id=instance.user_id,
        action=action
    ).save()


@receiver(pre_save, sender=CommentsVotes)
def comment_vote_changes(sender, instance: CommentsVotes, **kwargs):
    action = VoteAction.UPVOTED if instance.is_upvote else VoteAction.DOWNVOTED
    save_comment_vote_logs(instance, action)


@receiver(pre_delete, sender=CommentsVotes)
def comment_vote_deleted(sender, instance: CommentsVotes, **kwargs):
    action = VoteAction.CANCELLED_UPVOTE if instance.is_upvote else VoteAction.CANCELLED_DOWNVOTE
    save_comment_vote_logs(instance, action)


def save_comment_image_log(instance: CommentsImages):
    CommentImagesLogs(
        comment_id=instance.comment_id,
        image_url=instance.image_url
    ).save()


@receiver(pre_save, sender=CommentsImages)
def comment_images_created(sender, instance: CommentsImages, **kwargs):
    save_comment_image_log(instance)

