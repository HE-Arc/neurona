from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Spaces
from ..serializers import SpaceSerializer

# Get all spaces


@api_view(['GET'])
def get_spaces(request):
    spaces = Spaces.objects.all()
    serializer = SpaceSerializer(spaces, many=True)
    return Response(serializer.data)

# Get specific space by id


@api_view(['GET'])
def get_space(request, pk):
    try:
        space = Spaces.objects.get(pk=pk)
        serializer = SpaceSerializer(space)
        return Response(serializer.data)

    except Spaces.DoesNotExist:
        return Response({'error': 'Space not found'}, status=status.HTTP_404_NOT_FOUND)

# Create a space


@api_view(['POST'])
def create_space(request):
    serializer = SpaceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# Update a space by id, either with put or patch method


@api_view(['PUT', 'PATCH'])
def update_space(request, pk):
    try:
        space = Spaces.objects.get(pk=pk)
        if request.method == 'PUT':
            serializer = SpaceSerializer(space, data=request.data)
        elif request.method == 'PATCH':
            serializer = SpaceSerializer(
                space, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Spaces.DoesNotExist:
        return Response({'error': 'Space not found'}, status=status.HTTP_404_NOT_FOUND)


# Delete a space by id


@api_view(['DELETE'])
def delete_space(request, pk):
    try:
        space = Spaces.objects.get(pk=pk)
        space.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    except Spaces.DoesNotExist:
        return Response({'error': 'Space not found'}, status=status.HTTP_404_NOT_FOUND)

