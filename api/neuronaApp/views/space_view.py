from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Spaces
from ..serializers import SpaceSerializer

# Get all spaces


@api_view(['GET'])
def get_spaces(request):
    try:
        spaces = Spaces.objects.all()
        serializer = SpaceSerializer(spaces, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': 'Server error: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Get specific space by id


@api_view(['GET'])
def get_space(request, pk):
    try:
        space = Spaces.objects.get(pk=pk)
        serializer = SpaceSerializer(space)
        return Response(serializer.data)

    except Spaces.DoesNotExist:
        return Response({'error': 'Space not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': 'Server error: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Create a space


@api_view(['POST'])
def create_space(request):
    try:
        serializer = SpaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': 'Server error: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

    except Exception as e:
        return Response({'error': 'Server error: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Delete a space by id


@api_view(['DELETE'])
def delete_space(request, pk):
    try:
        space = Spaces.objects.get(pk=pk)
        space.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    except Spaces.DoesNotExist:
        return Response({'error': 'Space not found'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({'error': 'Server error: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
