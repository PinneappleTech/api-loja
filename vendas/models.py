from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from clientes.models import Cliente
from produtos.models import Produto

# Create your models here.
class Base(models.Model):
    criado_em     = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo         = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Venda(Base):
    DINHEIRO = 0
    CREDITO  = 1
    DEBITO   = 2
    CARNE    = 3

    FORMA_PAGAMENTO = (
        (DINHEIRO, "Dinheiro"),
        (CREDITO, "Credito"),
        (DEBITO, "Debito"),
        (CARNE, "Carnê")
    )

    cliente         = models.ForeignKey(Cliente, related_name="compras", on_delete=models.PROTECT)
    vendedor        = models.ForeignKey(User, related_name="vendas", on_delete=models.PROTECT)
    produtos        = models.ManyToManyField(Produto, through='ItemVenda')
    valor_total     = models.DecimalField(_("Valor Total"), max_digits=10, decimal_places=2)
    desconto        = models.PositiveIntegerField(_("Desconto"), null=True, blank=True)
    preco_final     = models.DecimalField(_("Preço Final"), max_digits=10, decimal_places=2)
    forma_pagamento = models.PositiveIntegerField(_("Forma de Pagamento"), choices=FORMA_PAGAMENTO)
    qtd_parcelas    = models.PositiveIntegerField(_("Quantidade de Parcelas"), null=True, blank=True)
    valor_parcelas  = models.DecimalField(_("Valor das Parcelas"), max_digits=10, decimal_places=2, null=True, blank=True)
    venc_parcelas   = models.DateField(_("Vencimento das Parcelas"), null=True, blank=True)

    
class ItemVenda(models.Model):
    produto        = models.ForeignKey(Produto, on_delete=models.PROTECT)
    venda          = models.ForeignKey(Venda, on_delete=models.CASCADE)
    quantidade     = models.PositiveIntegerField(_("Quantidade"))
    preco_unitario = models.DecimalField(_("Preço Unitário"), max_digits=10, decimal_places=2)
    preco_total    = models.DecimalField(_("Preço Total"), max_digits=10, decimal_places=2)