# Generated by Django 2.2.13 on 2020-07-31 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0018_auto_20200731_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='end_entrega',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='endereco',
        ),
        migrations.AddField(
            model_name='endereco',
            name='cliente',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='clientes.Cliente'),
        ),
    ]
