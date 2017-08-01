# -*- coding: utf-8 -*-
from django.db import models

class Cursos(models.Model):
    nome = models.CharField('Nome', max_length=30)
    descricao = models.TextField('Descrição')

    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.nome
