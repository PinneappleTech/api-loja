from rest_framework import serializers

from .models import Venda, ItemVenda


class VendaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venda
        fields = [
            'cliente',
            'vendedor',
            'produtos',
            'valor_total',
            'desconto',
            'preco_final',
            'forma_pagamento',
            'qtd_parcelas',
            'valor_parcelas',
            'venc_parcelas'
        ]


class VendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venda
        fields = [
            'id',
            'cliente',
            'vendedor',
            'valor_total',
            'desconto',
            'preco_final',
            'forma_pagamento',
            'qtd_parcelas',
            'valor_parcelas',
            'venc_parcelas',
            'criado_em',
            'atualizado_em',
            'ativo'
        ]
        read_only_fields = ['id', 'criado_em', 'atualizado_em']