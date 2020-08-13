from django.shortcuts import render
from rest_framework import generics

from .models import Fornecedor
from .serializers import FornecedorSerializer

# Create your views here.
class FornecedorListCreateView(generics.ListCreateAPIView):
    """
    Recurso para listar e criar Fornecedor
    """
    queryset = Fornecedor.objects.filter(ativo=True)
    serializer_class = FornecedorSerializer


class FornecedorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API para buscar, atualizar e deletar Fornecedor
    """
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer