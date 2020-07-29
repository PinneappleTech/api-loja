from rest_framework import serializers

from .models import Cliente, Endereco


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = [
            'endereco', 'bairro', 'cep', 'numero', 'uf', 'cidade', 'ponto_ref'
        ]

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'nome', 'cpf', 'rg', 'sexo', 'data_nasc', 'fone', 'email', 
            'estado_civil', 'conjuge', 'apelido', 'filiacao', 
            'credito', 'obs', 'criado_por', 'endereco', 'end_entrega'
        ]
