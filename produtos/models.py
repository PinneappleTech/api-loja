from django.db import models
from django.utils.translation import ugettext_lazy as _

from clientes.models import Endereco

# Create your models here.
class Base(models.Model):
    criado_em     = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo         = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Categoria(Base):
    nome = models.CharField(max_length=150, unique=True)

    def clean(self):
        self.nome = self.nome.upper()
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Marca(Base):
    nome = models.CharField(max_length=150, unique=True)

    def clean(self):
        self.nome = self.nome.upper()
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Produto(Base):
    categoria = models.ForeignKey(Categoria, related_name='categoria_produtos', on_delete=models.PROTECT)
    marca     = models.ForeignKey(Marca, related_name='marca_produtos', on_delete=models.PROTECT)
    nome      = models.CharField(max_length=150)
    estoque   = models.PositiveIntegerField()
    preco     = models.DecimalField(max_digits=10, decimal_places=2) #99.999.99,99
    descricao = models.TextField(null=True, blank=True)

    def clean(self):
        self.nome = self.nome.title()

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        unique_together = ['categoria', 'marca', 'nome']

    def __str__(self):
        return self.nome