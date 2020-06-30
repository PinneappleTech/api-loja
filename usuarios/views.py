from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Perfil
from .serializers import UsuarioSerializer, PerfilSerializer

# Create your views here.
class UsuariosViewset(viewsets.ModelViewSet):
    """
    API para listar e criar Usuários
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

    @action(detail=True, methods=['get'])
    def perfil(self, request, pk=None):
        usuario = self.get_object()
        try:
            serializer = PerfilSerializer(Perfil.objects.get(usuario_id=usuario.id))
            return Response(serializer.data)
        except Perfil.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # def create(self, request):
    #     for data in request.data:
    #         print(data)