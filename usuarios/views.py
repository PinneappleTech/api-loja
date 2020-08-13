from rest_framework import generics
from django.contrib.auth.models import User

from .serializers import UsuarioSerializer

# Create your views here.
###USUARIOS
class UsuariosGenericView(generics.ListCreateAPIView):
    """
    API para listar e criar Usuario
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioGenericView(generics.RetrieveUpdateDestroyAPIView):
    """
    API para buscar, atualizar e deletar Usuario
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer