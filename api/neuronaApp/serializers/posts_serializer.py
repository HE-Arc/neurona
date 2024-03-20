from rest_framework import serializers
from neuronaApp.models import Posts, Comments, PostsImages, CommentsImages, Votes, CommentsVotes
from neuronaApp.serializers.users_serializer import UserSerializer


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = [
            "user",
            "title",
            "content",
            "space",
            "tag",
        ]

class PostsUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Posts
        fields = [
            "user",
            "title",
            "content",
            "space",
            "tag",
        ]

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
