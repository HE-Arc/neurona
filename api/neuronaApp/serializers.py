from rest_framework import serializers
from .models import Posts, Comments, PostsImages, CommentsImages, Votes, CommentsVotes

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
