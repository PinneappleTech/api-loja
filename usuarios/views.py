from rest_framework import generics

from django.contrib.auth.models import User
from .serializers import UsuarioSerializer

# Create your views here.
class UsuariosGenericView(generics.ListCreateAPIView):
    """
    API para listar e criar Usuários
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer