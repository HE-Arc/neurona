import logging

from django.db.models import Q
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status, viewsets

from ..models import Spaces, Posts, SpacesAdmins, SpacesMembers
from ..pagination import PostsCursorPagination
from ..serializers import SpaceSerializer, PostsComplexSerializer
from ..token_authentication import TokenAuthentication

logger = logging.getLogger('django')

class SpacesViewSet(viewsets.ViewSet):
    queryset = Spaces.objects.all()
    authentication_classes = (TokenAuthentication,)

    def list(self, request):
        """Get all spaces."""
        spaces = Spaces.objects.all()
        serializer = SpaceSerializer(spaces, many=True, context=request.user)
        return Response(serializer.data)

    def create(self, request):
        """Create a new space."""
        serializer = SpaceSerializer(data=request.data, context=request.user)

        if serializer.is_valid():
            serializer.save()
            SpacesAdmins(user_id=request.user.id, space_id=serializer.instance.id).save()
            SpacesMembers(user_id=request.user.id, space_id=serializer.instance.id).save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Get a specific space by id."""
        try:
            space = Spaces.objects.get(pk=pk)
            serializer = SpaceSerializer(space, context=request.user)
            return Response(serializer.data)

        except Spaces.DoesNotExist:
            return Response({'error': 'Space not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Update a space by id with either put or patch method."""
        try:
            space = Spaces.objects.get(pk=pk)
            if request.method == 'PUT':
                serializer = SpaceSerializer(space, data=request.data, context=request.user)
            else:
                serializer = SpaceSerializer(
                    space, data=request.data, partial=True, context=request.user)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Spaces.DoesNotExist:
            return Response({'error': 'Space not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """Delete a space by id."""
        try:
            space = Spaces.objects.get(pk=pk)
            space.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Spaces.DoesNotExist:
            return Response({'error': 'Space not found'}, status=status.HTTP_404_NOT_FOUND)


    @action(detail=False, methods=['get'])
    def joined(self, request):
        spaces = Spaces.objects.filter(members__user=request.user)
        serializer = SpaceSerializer(spaces, many=True, context=request.user)
        return Response(serializer.data, status=200)


    @action(detail=True, methods=['get'])
    def posts(self, request, pk=None):
        posts = Spaces.objects.get(pk=pk).posts
        paginator = PostsCursorPagination()
        page = paginator.paginate_queryset(posts, request, view=self)

        if page is not None:
            serializer = PostsComplexSerializer(page, context=request.user, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = PostsComplexSerializer(posts, context=request.user, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.GET.get('q', default="")
        spaces = Spaces.objects.filter(Q(name__icontains=query) | Q(about__icontains=query))
        serializer = SpaceSerializer(spaces, many=True, context=request.user)
        return Response(serializer.data, status=200)

    def _join(self, request, pk=None):
        assert request.method == 'POST'
        if SpacesMembers.objects.filter(user_id=request.user.id, space_id=pk).exists():
            return Response({}, status=200)

        SpacesMembers(user_id=request.user.id, space_id=pk).save()
        return Response({}, status=201)

    def _quit(self, request, pk=None):
        assert request.method == 'DELETE'
        if not SpacesMembers.objects.filter(user_id=request.user.id, space_id=pk).exists():
            return Response({}, status=200)

        SpacesMembers.objects.filter(user_id=request.user.id, space_id=pk).delete()
        return Response({}, status=204)


    @action(detail=True, methods=['post', 'delete'])
    def join(self, request, pk=None):
        if request.method == 'POST':
            return self._join(request, pk)

        else:
            return self._quit(request, pk)