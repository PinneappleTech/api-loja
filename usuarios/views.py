from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User

#from .models import Perfil
from .serializers import UsuarioSerializer

# Create your views here.
class UsuariosViewset(viewsets.ModelViewSet):
    """
    API para listar e criar Usuários
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer