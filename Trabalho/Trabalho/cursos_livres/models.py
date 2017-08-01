# -*- coding: utf-8 -*-
from django.db import models

class CursosLivres(models.Model):

    nome = models.CharField('Nome', max_length=30)
    data = models.DateField('Data do Curso')
    hora_inicio = models.TimeField('Horário de Início do Curso')
    hora_fim = models.TimeField('Horário de Fim do Curso')
    pagseguro = models.TextField('Botão Pagseguro', max_length=600)
    #evento = models.CharField("Link do evento no Facebook", max_length=100)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return '%s - %s' %(self.nome, self.created_at)
