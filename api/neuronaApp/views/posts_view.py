from django.shortcuts import render
from rest_framework import viewsets
from neuronaApp.models import Posts, Comments
from neuronaApp.serializers import PostsSerializer, CommentsSerializer

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
