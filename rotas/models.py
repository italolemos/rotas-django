from django.db import models


class Rotas(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.CharField('Descrição', max_length=500)
    tamanho = models.DecimalField('Tamanho da Rota em Km', max_digits=4, decimal_places=2)

    def __str__(self):
        return self.nome
