from rest_framework import generics
from rest_framework.response import Response

from .models import Categoria, Marca, Produto
from .serializers import CategoriaSerializer, MarcaSerializer, ProdutoSerializer, ProdutoCreateSerializer

# Create your views here.
#CATEGORIA
class CategoriaList(generics.ListCreateAPIView):
    """
    Recurso para listar e criar Categoria
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Recurso para buscar, atualizar e deletar Categoria
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


#MARCA
class MarcaList(generics.ListCreateAPIView):
    """
    Recurso para listar e criar Marca
    """
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class MarcaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Recurso para buscar, atualizar e deletar Marca
    """
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

#PRODUTO
class ProdutoList(generics.ListCreateAPIView):
    """
    Recurso para listar e criar Produto
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Recurso para buscar, atualizar e deletar Produto
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
