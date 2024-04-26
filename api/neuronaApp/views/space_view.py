from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from ..models import Spaces
from ..serializers import SpaceSerializer


class SpacesViewSet(viewsets.ViewSet):
    queryset = Spaces.objects.all()

    def list(self, request):
        """Get all spaces."""
        spaces = Spaces.objects.all()
        serializer = SpaceSerializer(spaces, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new space."""
        serializer = SpaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Get a specific space by id."""
        try:
            space = Spaces.objects.get(pk=pk)
            serializer = SpaceSerializer(space)
            return Response(serializer.data)

        except Spaces.DoesNotExist:
            return Response({'error': 'Space not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Update a space by id with either put or patch method."""
        try:
            space = Spaces.objects.get(pk=pk)
            if request.method == 'PUT':
                serializer = SpaceSerializer(space, data=request.data)
            else:
                serializer = SpaceSerializer(
                    space, data=request.data, partial=True)

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
