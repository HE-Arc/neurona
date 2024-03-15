from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Spaces
from ..serializers import SpaceSerializer

@api_view(['GET'])
def test(request):
    try:
        return Response({"message": "Hello World"})
    except Exception as e:
        return Response({'error': 'Server error: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_spaces(request):
    try:
        if request.method == 'GET':
            spaces = Spaces.objects.all()
            serializer = SpaceSerializer(spaces, many=True)
            return Response(serializer.data)
    except Exception as e:
        return Response({'error': 'Server error: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def create_space(request):
    try:
        if request.method == 'POST':
            serializer = SpaceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        # Pour un debug, loguer l'exception ou renvoyer une réponse détaillée peut aider.
        # Assurez-vous de ne pas exposer d'informations sensibles en production.
        return Response({'error': 'Server error: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
