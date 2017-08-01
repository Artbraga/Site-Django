# -*- coding: utf-8 -*-
from django.db import models

class Turmas(models.Model):

    nome = models.CharField('Nome', max_length=50)
    dia = models.CharField('Dia(s) da semana', max_length=30)
    data_inicio = models.DateField('Data de Início')

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return '%s-%s' % (self.nome, self.data_inicio.strftime("%d/%m/%y"))
