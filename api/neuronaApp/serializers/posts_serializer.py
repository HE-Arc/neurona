from rest_framework import serializers
from neuronaApp.models import Posts, Comments, CommentsImages, Votes, CommentsVotes, SavedPosts
from neuronaApp.serializers.users_serializer import UserSerializer


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = [
            "user",
            "content",
            "space",
            "tag",
            "image_urls"
        ]

    def create(self, validated_data):
        return Posts.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.image_urls = validated_data.get('image_urls', instance.image_urls)
        instance.save()
        return instance

class PostsComplexSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    votes_and_comments = serializers.SerializerMethodField()
    is_saved = serializers.SerializerMethodField()
    image_urls = serializers.ListField(child=serializers.URLField())


    class Meta:
        model = Posts
        fields = [
            "id",
            "user",
            "votes_and_comments",
            "created_at",
            "content",
            "space",
            "tag",
            "is_saved",
            "image_urls"
        ]

    def update(self, instance, validated_data):
        instance.image_urls = validated_data.get('image_urls', instance.image_urls)
        instance.save()
        return instance

    def get_votes_and_comments(self, obj):
        votes = obj.get_vote_count()
        comments = obj.get_comments_count()
        has_upvoted = obj.has_upvoted(self.context)
        has_downvoted = obj.has_downvoted(self.context)
        return {
            "votes": votes,
            "comments": comments,
            "has_upvoted": has_upvoted,
            "has_downvoted": has_downvoted
        }

    def get_is_saved(self, obj):
        return obj.is_saved(self.context)


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            "user",
            "post",
            "content"
        ]

class CommentsComplexSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    votes = serializers.SerializerMethodField()
    class Meta:
        model = Comments
        fields = [
            "id",
            "user",
            "votes",
            "created_at",
            "content"
        ]

    def get_votes(self, obj):
        votes = obj.get_vote_count()
        has_upvoted = obj.has_upvoted(self.context)
        has_downvoted = obj.has_downvoted(self.context)
        return {
            "votes": votes,
            "has_upvoted": has_upvoted,
            "has_downvoted": has_downvoted
        }


class VotesAndCommentsSerializers(serializers.Serializer):
    votes = serializers.IntegerField()
    comments = serializers.IntegerField()
    has_upvoted = serializers.BooleanField()
    has_downvoted = serializers.BooleanField()