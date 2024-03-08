from django.shortcuts import render
from rest_framework import viewsets
from .models import Posts, Comments
from .serializers import PostsSerializer, CommentsSerializer

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
