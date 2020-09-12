from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from .serializers import UsuarioSerializer
from .models import Perfil

# Create your views here.
###USUARIOS
class UsuariosGenericView(generics.ListCreateAPIView):
    """
    API para listar e criar Usuario
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):
        cpfExist = Perfil.objects.filter(cpf=self.request.data['cpf'])
        if cpfExist.exists():
            raise ValidationError({ "cpf": ["Um usuário com este CPF já existe."] })
        serializer.save()



class UsuarioGenericView(generics.RetrieveUpdateDestroyAPIView):
    """
    API para buscar, atualizar e deletar Usuario
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer