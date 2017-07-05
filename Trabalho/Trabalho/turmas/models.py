from django.db import models
from datetime import datetime

class Turmas(models.Model):

    nome = models.CharField('Nome', max_length=50)
    dia = models.CharField('Dia(s) da semana', max_length=30)
    data_inicio = models.DateField('Data de Início')

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return '%s-%s' % (self.nome, self.data_inicio.strftime("%d/%m/%y"))


# turmass = []
# turmass.append(Turmas(nome="Técnico de Enfermagem", dia="Sábado de 8:00 às 13:00",data_inicio="2017-02-04"))
# turmass.append(Turmas(nome="Técnico de Enfermagem", dia="Sábado de 8:00 às 13:00",data_inicio="2017-02-04"))
# turmass.append(Turmas(nome="Especialização em Instrumentação Cirúrgica", dia="Terça de 9:00 às 13:00",data_inicio="2017-02-14"))
# turmass.append(Turmas(nome="Especialização em Instrumentação Cirúrgica", dia="Quinta de 14:00 às 18:00",data_inicio="2017-03-23"))
# turmass.append(Turmas(nome="Técnico de Enfermagem", dia="Quarta e Sexta de 9:00 às 12:00",data_inicio="2017-04-19"))
# turmass.append(Turmas(nome="Especialização em Instrumentação Cirúrgica", dia="Quarta de 17:00 às 21:00",data_inicio="2017-04-19"))
# turmass.append(Turmas(nome="Especialização em Instrumentação Cirúrgica", dia="Quarta de 9:00 às 13:00",data_inicio="2017-05-31"))
# turmass.append(Turmas(nome="Especialização em Instrumentação Cirúrgica", dia="Sábado de 8:00 às 12:00",data_inicio="2017-06-24"))
# turmass.append(Turmas(nome="Especialização em Instrumentação Cirúrgica", dia="Quarta de 14:00 às 18:00",data_inicio="2017-07-19"))
# for turma in turmass:
#     turma.save()