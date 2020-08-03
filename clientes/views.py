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
        serializer_end = EnderecoSerializer(data=serializer.validated_data['endereco'])
        serializer_end.is_valid(raise_exception=True)
        end = serializer_end.save()
        serializer.is_valid(raise_exception=True)
        serializer.save(criado_por=self.request.user, ativo=True, endereco=end)
        

class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API para buscar, atualizar e deletar Cliente
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer_end = EnderecoSerializer(instance.endereco, data=request.data, partial=partial)
        serializer_end.is_valid(raise_exception=True)
        self.perform_update(serializer_end)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_destroy(self, instance):
        try:
            instance.endereco.delete()
            instance.delete()
        except ProtectedError as error:
            raise ValidationError(error)

        