from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Cliente, Endereco
from .serializers import ClienteSerializer, EnderecoSerializer

# Create your views here.
class ClienteAPIView(APIView):
    """
    API de Clientes
    """
    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class EnderecoAPIView(APIView):
    """
    API de Endereços de Clientes
    """
    def get(self, request):
        enderecos = Endereco.objects.all()
        serializer = EnderecoSerializer(enderecos, many=True)
        return Response(serializer.data)