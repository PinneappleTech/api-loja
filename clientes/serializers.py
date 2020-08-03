from rest_framework import serializers

from .models import Cliente, Endereco

# Campos Obrigatorios
# endereço, bairro, cep, uf, cidade, criado_em, atualizado_em, ativo
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = [
            'logradouro',
            'bairro',
            'cep',
            'numero',
            'uf',
            'cidade',
            'ponto_ref',
            'criado_em',
            'atualizado_em'
        ]

# Campos Obrigatorios
# nome, cpf, sexo, data_nasc, fone, estado_civil, filiação
# status, credito, criado_por, endereço criado_em, atualizado_em, ativo
class ClienteSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    end_entrega = EnderecoSerializer(read_only=True)

    class Meta:
        model = Cliente
        fields = [
            'id',
            'nome',
            'cpf',
            'rg',
            'sexo',
            'data_nasc',
            'fone',
            'fone_recado',
            'email',
            'estado_civil',
            'conjuge',
            'apelido',
            'filiacao',
            'status',
            'credito',
            'obs',
            'criado_por',
            'criado_em',
            'atualizado_em',
            'ativo',
            'endereco',
            'end_entrega'
        ]
        read_only_fields = ['id', 'criado_por', 'criado_em', 'atualizado_em']