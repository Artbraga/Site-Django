# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeArquivo', models.CharField(max_length=30, verbose_name='Noome do arquivo')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descricao')),
                ('referencia', models.CharField(max_length=20, verbose_name='Secao')),
            ],
        ),
    ]
