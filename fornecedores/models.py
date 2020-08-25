from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from clientes.models import Endereco

# Create your models here.
class Base(models.Model):
    criado_em     = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo         = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Fornecedor(Base):
    nome     = models.CharField(max_length=150)
    cnpj     = models.CharField(max_length=14, unique=True)
    fone     = models.CharField(max_length=11)
    email    = models.EmailField(null=True, blank=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)