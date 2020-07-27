from rest_framework import generics
from django.contrib.auth.models import User

from .serializers import UsuarioSerializer

# Create your views here.
###USUARIOS
class UsuariosGenericView(generics.ListCreateAPIView):
    """
    API para listar e criar Usuario
    """
    queryset = User.objects.filter(is_active=True)
    serializer_class = UsuarioSerializer

class UsuarioGenericView(generics.RetrieveUpdateDestroyAPIView):
    """
    API para buscar, atualizar e deletar Usuario
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()