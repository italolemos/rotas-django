# Generated by Django 3.0.4 on 2020-03-24 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotas', '0002_auto_20200324_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rotas',
            name='tamanho',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Tamanho da Rota em Km'),
        ),
    ]
