# Generated by Django 2.2.13 on 2020-07-30 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_auto_20200620_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='criado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='clientes', to=settings.AUTH_USER_MODEL),
        ),
    ]
