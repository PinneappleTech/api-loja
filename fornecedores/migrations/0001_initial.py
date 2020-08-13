# Generated by Django 2.2.13 on 2020-08-05 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0023_auto_20200801_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=150)),
                ('cnpj', models.CharField(max_length=14)),
                ('fone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.Endereco')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
