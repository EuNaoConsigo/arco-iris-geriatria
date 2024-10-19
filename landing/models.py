
from django.db import models


class Avaliacao(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens/')
    avaliacao = models.TextField()
    estrelas = models.PositiveIntegerField(choices=[(i, i) for i in range(6)])

    def __str__(self):
        return self.nome
