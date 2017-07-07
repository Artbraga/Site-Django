from django.db import models

class Imagem(models.Model):

    nomeArquivo = models.CharField('Noome do arquivo', max_length=30)
    descricao = models.CharField('Descricao', max_length=50)
    referencia = models.CharField('Secao', max_length=20)

    def __str__(self):
        return self.nomeArquivo