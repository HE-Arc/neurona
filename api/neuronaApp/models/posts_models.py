from django.db import models

class Posts(models.Model):
    user = models.ForeignKey('User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    space = models.ForeignKey('Spaces', related_name='posts', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tags', related_name='posts', on_delete=models.CASCADE)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostsImages(models.Model):
    post = models.ForeignKey(Posts, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    user = models.ForeignKey('User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CommentsImages(models.Model):
    comment = models.ForeignKey(Comments, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Votes(models.Model):
    user = models.ForeignKey('User', related_name='votes', on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, related_name='votes', on_delete=models.CASCADE)
    is_upvote = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)