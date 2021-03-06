# Generated by Django 2.2.13 on 2020-06-16 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20200615_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='fone',
            field=models.CharField(max_length=11, null=True, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='data_nasc',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='tipo_usuario',
            field=models.PositiveSmallIntegerField(choices=[(1, 'VENDEDOR'), (2, 'CAIXA'), (3, 'SUPERVISOR'), (4, 'ADMINISTRADOR')], default=1, verbose_name='Tipo de Usuário'),
        ),
    ]
