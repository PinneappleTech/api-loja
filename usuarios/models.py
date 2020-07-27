from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class Perfil(models.Model):
    SEXO = (
        ('F', 'FEMININO'),
        ('M', 'MASCULINO'),
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

    usuario = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE, default=True)
    tipo_usuario = models.PositiveSmallIntegerField(_('Tipo de Usuário'), choices=TIPOS_USUARIOS, default=VENDEDOR)
    sexo = models.CharField(max_length=1, choices=SEXO)
    fone = models.CharField(_('Telefone'), max_length=11, null=True, blank=True)
    cpf = models.CharField(max_length=11)
    data_nasc = models.DateField(_('Data de Nascimento'), null=True, blank=True)

