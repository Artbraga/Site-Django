# -*- coding: utf-8 -*-
from django.db import models

class Utilidades(models.Model):
    atributo = models.CharField("Mês", max_length=20)
    valor = models.CharField("Mês", max_length=50)

    def __str__(self):
        return self.atributo
