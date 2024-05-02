from django.db import models

class Posts(models.Model):
    user = models.ForeignKey('User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    space = models.ForeignKey('Spaces', related_name='posts', on_delete=models.CASCADE, null=True)
    tag = models.ForeignKey('Tags', related_name='posts', on_delete=models.CASCADE, null=True)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_vote_count(self):
        return self.votes.filter(is_upvote=True).count() - self.votes.filter(is_upvote=False).count()

    def get_comments_count(self):
        return self.comments.count()

    def has_upvoted(self, user):
        return self.votes.filter(user=user, is_upvote=True).exists()

    def has_downvoted(self, user):
        return self.votes.filter(user=user, is_upvote=False).exists()

    def upvote(self, user):
        vote = self.votes.filter(user=user).first()
        if vote:
            vote.is_upvote = True
            vote.save()
        else:
            Votes.objects.create(user=user, post=self, is_upvote=True)

    def downvote(self, user):
        vote = self.votes.filter(user=user).first()
        if vote:
            vote.is_upvote = False
            vote.save()
        else:
            Votes.objects.create(user=user, post=self, is_upvote=False)

    def unvote(self, user):
        vote = self.votes.filter(user=user).first()
        if vote:
            vote.delete()

    def is_saved(self, user):
        return self.saved.filter(user=user).exists()




class Comments(models.Model):
    user = models.ForeignKey('User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_vote_count(self):
        return self.votes.filter(is_upvote=True).count() - self.votes.filter(is_upvote=False).count()

    def has_upvoted(self, user):
        return self.votes.filter(user=user, is_upvote=True).exists()

    def has_downvoted(self, user):
        return self.votes.filter(user=user, is_upvote=False).exists()

    def upvote(self, user):
        vote = self.votes.filter(user=user).first()
        if vote:
            vote.is_upvote = True
            vote.save()
        else:
            CommentsVotes.objects.create(user=user, comment=self, is_upvote=True)

    def downvote(self, user):
        vote = self.votes.filter(user=user).first()
        if vote:
            vote.is_upvote = False
            vote.save()
        else:
            CommentsVotes.objects.create(user=user, comment=self, is_upvote=False)

    def unvote(self, user):
        vote = self.votes.filter(user=user).first()
        if vote:
            vote.delete()



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


class CommentsVotes(models.Model):
    user = models.ForeignKey('User', related_name='comments_votes', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, related_name='votes', on_delete=models.CASCADE)
    is_upvote = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SavedPosts(models.Model):
    user = models.ForeignKey('User', related_name='saved', on_delete=models.CASCADE)
    post = models.ForeignKey('Posts', related_name='saved', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostsImages(models.Model):
    post = models.ForeignKey(Posts, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
