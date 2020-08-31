# Generated by Django 2.2.13 on 2020-08-25 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_auto_20200806_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='marca_produtos', to='produtos.Marca'),
        ),
    ]
