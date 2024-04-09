from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from neuronaApp.models import Posts, Comments
from neuronaApp.serializers import PostsSerializer, CommentsSerializer, UserSerializer, PostsComplexSerializer
from neuronaApp.token_authentication import TokenAuthentication
from neuronaApp.views.authentication_view import logger


class PostsViewSet(viewsets.ViewSet):
    queryset = Posts.objects.all()
    authentication_classes = (TokenAuthentication,)

    def list(self, request, *args, **kwargs):
        queryset = Posts.objects.all()
        serializer = PostsComplexSerializer(queryset, context=request.user, many=True)

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


class VoteView(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)

    @action(detail=True, methods=["post"])
    def upvote(self, request, pk):
        post = Posts.objects.get(pk=pk)
        user = request.user
        post.upvote(user)
        return Response(status=200)

    @action(detail=True, methods=["post"])
    def downvote(self, request, pk):
        post = Posts.objects.get(pk=pk)
        user = request.user
        post.downvote(user)
        return Response(status=200)

    @action(detail=True, methods=["post"])
    def unvote(self, request, pk):
        post = Posts.objects.get(pk=pk)
        user = request.user
        post.unvote(user)
        return Response(status=200)