# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turmas',
            name='data_inicio',
            field=models.DateField(verbose_name=b'Data de In\xc3\xadcio'),
        ),
    ]
