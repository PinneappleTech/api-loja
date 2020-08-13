from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db.models import ProtectedError

from .models import Cliente
from .serializers import ClienteSerializer, EnderecoSerializer

###CLIENTES
class ClienteListCreateView(generics.ListCreateAPIView):
    """
    Recurso para listar e criar Cliente
    """
    queryset = Cliente.objects.filter(ativo=True)
    serializer_class = ClienteSerializer

    def perform_create(self, serializer):
        serializer.save(criado_por=self.request.user, ativo=True)
        

class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API para buscar, atualizar e deletar Cliente
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def perform_destroy(self, instance):
        try:
            if instance.endereco is not None:
                instance.endereco.delete()
            if instance.end_entrega is not None:
                instance.end_entrega.delete()
            instance.delete()
        except ProtectedError as error:
            raise ValidationError(error)

        