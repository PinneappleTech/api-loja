from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    SEXO = (
        (1, 'FEMININO'),
        (2, 'MASCULINO'),
    )

    VENDEDOR = 1
    CAIXA = 2
    SUPERVISOR = 3
    ADMIN = 4

    TIPOS_USUARIOS = (
        (VENDEDOR, 'VENDEDOR'),
        (CAIXA, 'CAIXA'),
        (SUPERVISOR, 'SUPERVISOR'),
        (ADMIN, 'ADMINISTRADOR'),
    )

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, default=True)
    tipo_usuario = models.PositiveSmallIntegerField(choices=TIPOS_USUARIOS, default=VENDEDOR)
    sexo = models.PositiveSmallIntegerField(choices=SEXO)
    cpf = models.CharField(max_length=11)
    data_nasc = models.DateField()