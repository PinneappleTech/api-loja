from rest_framework import serializers

from .models import Categoria, Marca, Produto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']
        read_only_fields = ['id']


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nome']
        read_only_fields = ['id']


class ProdutoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = [
            'categoria',
            'marca',
            'descricao',
            'estoque',
            'estoque_min',
            'preco',
            'genero',
            'tipo',
            'tamanho'
        ]


class ProdutoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    marca     = serializers.StringRelatedField()

    class Meta:
        model = Produto
        fields = [
            'id',
            'categoria',
            'marca',
            'descricao',
            'estoque',
            'estoque_min',
            'preco',
            'genero',
            'tipo',
            'tamanho',
            'criado_em',
            'atualizado_em',
            'ativo'
        ]
        read_only_fields = ['id', 'criado_em', 'atualizado_em']