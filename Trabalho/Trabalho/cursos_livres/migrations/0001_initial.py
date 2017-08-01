# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CursosLivres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30, verbose_name=b'Nome')),
                ('data', models.DateField(verbose_name=b'Data do Curso')),
                ('hora_inicio', models.TimeField(verbose_name=b'Hor\xc3\xa1rio de In\xc3\xadcio do Curso')),
                ('hora_fim', models.TimeField(verbose_name=b'Hor\xc3\xa1rio de Fim do Curso')),
                ('pagseguro', models.CharField(max_length=500, verbose_name=b'Mensagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em')),
            ],
        ),
    ]
