from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .models import Perfil


class UsuarioSerializer(serializers.ModelSerializer):
    tipo_usuario = serializers.ChoiceField(source='perfil.tipo_usuario', choices=Perfil.TIPOS_USUARIOS)
    sexo = serializers.ChoiceField(source='perfil.sexo', choices=Perfil.SEXO)
    fone = serializers.CharField(source='perfil.fone', max_length=11, min_length=11, style={'input_type': 'number'}, required=False)
    cpf = serializers.CharField(source='perfil.cpf', max_length=11, min_length=11, style={'input_type': 'number'})
    data_nasc = serializers.DateField(source='perfil.data_nasc', required=False)

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
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        perfil_data = validated_data.pop('perfil')
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['is_active'] = True
        usuario = User.objects.create(**validated_data)
        Perfil.objects.create(usuario=usuario, **perfil_data)
        return usuario

    def update(self, instance, validated_data):
        for field in validated_data:
            if field == 'perfil':
                for field in validated_data['perfil']:
                    setattr(instance.perfil, field, validated_data.get('perfil').get(field, getattr(instance.perfil, field)))
                instance.perfil.save()
            else:
                setattr(instance, field, validated_data.get(field, getattr(instance, field)))
        instance.save()
        return instance