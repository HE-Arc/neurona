from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from neuronaApp.models import Posts, Comments, User
from neuronaApp.serializers import PostsSerializer, CommentsSerializer, UserSerializer, PostsComplexSerializer, \
    CommentsComplexSerializer
from neuronaApp.token_authentication import TokenAuthentication
from neuronaApp.views.authentication_view import logger


class PostsViewSet(viewsets.ViewSet):
    queryset = Posts.objects.all()
    authentication_classes = (TokenAuthentication,)

    def destroy(self, request, pk=None):
        post = get_object_or_404(Posts, pk=pk)

        if request.user.id != post.user_id:
            return Response({"message": "You cannot delete this post because you aren't its author"}, status=403)

        post.delete()
        return Response(status=204)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(Posts, pk=pk)
        serializer = PostsComplexSerializer(post, context=request.user, many=False)

        return Response(serializer.data, 200)

    def list(self, request, *args, **kwargs):
        queryset = Posts.objects.all()
        serializer = PostsComplexSerializer(queryset, context=request.user, many=True)

        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path='user/(?P<username>[^/.]+)')
    def user(self, request, username=None):
        user_id = get_object_or_404(User, username__exact=username).id
        queryset = Posts.objects.filter(user_id__exact=user_id)
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


    @action(detail=True, methods=['get'], url_path='comments')
    def get_comments(self, request, pk=None):
        comments = Comments.objects.filter(post_id=pk)
        serializer = CommentsComplexSerializer(comments, context=request.user, many=True)

        return Response(serializer.data, status=200)

    @get_comments.mapping.post
    def create_comment(self, request, pk=None):
        data = request.data.copy()
        data['user'] = request.user.id
        data['post'] = pk
        serializer = CommentsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class CommentsViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)

    def destroy(self, request, pk=None):
        comment = get_object_or_404(Comments, pk=pk)

        if request.user.id != comment.user_id:
            return Response({"message": "You cannot delete this comment because you aren't its author"}, status=403)

        comment.delete()
        return Response(status=204)

    @action(detail=True, methods=["post"])
    def upvote(self, request, pk=None):
        comment = get_object_or_404(Comments, pk=pk)
        comment.upvote(request.user)
        return Response(status=200)

    @action(detail=True, methods=["post"])
    def downvote(self, request, pk=None):
        comment = get_object_or_404(Comments, pk=pk)
        comment.downvote(request.user)
        return Response(status=200)

    @action(detail=True, methods=["post"])
    def unvote(self, request, pk=None):
        comment = get_object_or_404(Comments, pk=pk)
        comment.unvote(request.user)
        return Response(status=200)

class VoteView(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)

    @action(detail=True, methods=["post"])
    def upvote(self, request, pk):
        post = get_object_or_404(Posts, pk=pk)
        user = request.user
        post.upvote(user)
        return Response(status=200)

    @action(detail=True, methods=["post"])
    def downvote(self, request, pk):
        post = get_object_or_404(Posts, pk=pk)
        user = request.user
        post.downvote(user)
        return Response(status=200)

    @action(detail=True, methods=["post"])
    def unvote(self, request, pk):
        post = get_object_or_404(Posts, pk=pk)
        user = request.user
        post.unvote(user)
        return Response(status=200)