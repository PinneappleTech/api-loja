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
            'nome',
            'estoque',
            'preco',
            'genero',
            'tipo',
            'tamanho',
            'descricao'
        ]


class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    marca     = MarcaSerializer(required=False)

    class Meta:
        model = Produto
        fields = [
            'id',
            'categoria',
            'marca',
            'nome',
            'estoque',
            'preco',
            'genero',
            'tipo',
            'tamanho',
            'descricao',
            'criado_em',
            'atualizado_em',
            'ativo'
        ]
        read_only_fields = ['id', 'criado_em', 'atualizado_em']