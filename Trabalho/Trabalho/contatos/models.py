from django.db import models
from .forms import ContatoCurso

class Contato(models.Model):

    nome = models.CharField('Nome (obrigatório)', max_length=30)
    email = models.EmailField('E-mail (obrigatório)', max_length=30)
    assunto = models.CharField('Assunto (obrigatório)' , max_length=30)
    mensagem = models.CharField('Mensagem (obrigatório)', max_length=300)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return '%s - %s' %(self.nome, self.created_at)
