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
    #perfil = PerfilSerializer()
    tipo_usuario = serializers.ChoiceField(source='perfil.tipo_usuario', choices=Perfil.TIPOS_USUARIOS)
    sexo = serializers.ChoiceField(source='perfil.sexo', choices=Perfil.SEXO)
    fone = serializers.CharField(source='perfil.fone')
    cpf = serializers.CharField(source='perfil.cpf')
    data_nasc = serializers.DateField(source='perfil.data_nasc')

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'last_login',
            'date_joined',
            'tipo_usuario',
            'sexo',
            'fone',
            'cpf',
            'data_nasc',
        )
        read_only_fields = ['id', 'last_login', 'date_joined']

    def create(self, validated_data):
        perfil_data = validated_data.pop('perfil')
        usuario = User.objects.create(**validated_data)
        Perfil.objects.create(usuario=usuario, **perfil_data)
        return usuario