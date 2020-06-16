# Generated by Django 2.2.13 on 2020-06-16 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20200614_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(error_messages={'unique': 'Um Cliente com este mesmo CPF já existe.'}, max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='estado_civil',
            field=models.PositiveSmallIntegerField(choices=[(1, 'CASADO(A)'), (2, 'DIVORCIADO(A)'), (3, 'SEPARADO(A)'), (4, 'SOLTEIRO(A)'), (5, 'VIUVO(A)')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.PositiveSmallIntegerField(choices=[(1, 'FEMININO'), (2, 'MASCULINO')]),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
