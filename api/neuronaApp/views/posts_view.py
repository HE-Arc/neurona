from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from neuronaApp.models import Posts, Comments
from neuronaApp.serializers import PostsSerializer, CommentsSerializer, UserSerializer, PostsUserSerializer
from neuronaApp.token_authentication import TokenAuthentication
from neuronaApp.views.authentication_view import logger


class PostsViewSet(viewsets.ViewSet):
    queryset = Posts.objects.all()
    authentication_classes = (TokenAuthentication,)

    def list(self, request, *args, **kwargs):
        queryset = Posts.objects.all()
        serializer = PostsUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data.copy()
        data['user'] = user.id
        serializer = PostsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
