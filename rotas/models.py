from django.db import models


class Rotas(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.CharField('Descrição', max_length=200)
    tamanho = models.DecimalField('Tamanho da Rota em Km', max_digits=3, decimal_places=1)


