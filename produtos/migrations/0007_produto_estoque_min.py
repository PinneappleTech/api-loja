# Generated by Django 2.2.13 on 2020-08-31 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0006_auto_20200824_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='estoque_min',
            field=models.PositiveIntegerField(default=1, verbose_name='Estoque Mínimo'),
        ),
    ]
