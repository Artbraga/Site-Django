# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos_livres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursoslivres',
            name='pagseguro',
            field=models.TextField(max_length=600, verbose_name=b'Bot\xc3\xa3o Pagseguro'),
        ),
    ]
