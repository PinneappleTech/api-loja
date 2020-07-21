from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Perfil

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = (
            'tipo_usuario',
            'sexo',
            'fone',
            'cpf',
            'data_nasc',
        )

class UsuarioSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer()

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'last_login',
            'date_joined',
            'perfil',
        )
        read_only_fields = ['last_login', 'date_joined', 'perfil']