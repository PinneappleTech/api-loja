# Generated by Django 2.2.13 on 2020-07-24 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20200622_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='data_nasc',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='fone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Telefone'),
        ),
    ]
