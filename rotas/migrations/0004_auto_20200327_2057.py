# Generated by Django 3.0.4 on 2020-03-27 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rotas', '0003_auto_20200324_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rotas',
            name='descricao',
            field=models.CharField(max_length=500, verbose_name='Descrição'),
        ),
    ]
