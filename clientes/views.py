from rest_framework import generics

from .models import Cliente, Endereco
from .serializers import ClienteSerializer, EnderecoSerializer

###CLIENTES
class ClientesGenericView(generics.ListCreateAPIView):
    """
    API para listar e criar Cliente
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteGenericView(generics.RetrieveUpdateDestroyAPIView):
    """
    API para buscar, atualizar e deletar Cliente
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

###Enderecos
class EnderecosGenericView(generics.ListCreateAPIView):
    """
    API para listar e criar Enderecos
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class EnderecoGenericView(generics.RetrieveUpdateDestroyAPIView):
    """
    API para buscar, atualizar e deletar endereco
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer