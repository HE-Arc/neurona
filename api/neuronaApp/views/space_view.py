from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Spaces
from ..serializers import SpaceSerializer

class SpaceView(APIView):
    def get(self, request, pk=None):
        if pk:
            # Get a specific space by id
            try:
                space = Spaces.objects.get(pk=pk)
                serializer = SpaceSerializer(space)
                return Response(serializer.data)
            except Spaces.DoesNotExist:
                return Response({'error': 'Space not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Get all spaces
            spaces = Spaces.objects.all()
            serializer = SpaceSerializer(spaces, many=True)
            return Response(serializer.data)

    def post(self, request):
        # Create a new space
        serializer = SpaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        # Update a space by id with PUT method
        try:
            space = Spaces.objects.get(pk=pk)
            serializer = SpaceSerializer(space, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Spaces.DoesNotExist:
            return Response({'error': 'Space not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        # Update a space by id with PATCH method
        try:
            space = Spaces.objects.get(pk=pk)
            serializer = SpaceSerializer(
                space, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Spaces.DoesNotExist:
            return Response({'error': 'Space not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        # Delete a space by id
        try:
            space = Spaces.objects.get(pk=pk)
            space.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Spaces.DoesNotExist:
            return Response({'error': 'Space not found'}, status=status.HTTP_404_NOT_FOUND)
