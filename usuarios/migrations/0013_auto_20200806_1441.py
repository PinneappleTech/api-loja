# Generated by Django 2.2.13 on 2020-08-06 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_auto_20200727_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='estado_civil',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'CASADO(A)'), (2, 'DIVORCIADO(A)'), (3, 'SEPARADO(A)'), (4, 'SOLTEIRO(A)'), (5, 'VIUVO(A)')], null=True, verbose_name='Estado Civil'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='obs',
            field=models.TextField(blank=True, null=True),
        ),
    ]
