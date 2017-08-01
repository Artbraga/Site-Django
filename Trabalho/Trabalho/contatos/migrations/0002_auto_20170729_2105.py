# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='assunto',
            field=models.CharField(max_length=30, verbose_name=b'Assunto (obrigat\xc3\xb3rio)'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.EmailField(max_length=30, verbose_name=b'E-mail (obrigat\xc3\xb3rio)'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='mensagem',
            field=models.CharField(max_length=300, verbose_name=b'Mensagem (obrigat\xc3\xb3rio)'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='nome',
            field=models.CharField(max_length=30, verbose_name=b'Nome (obrigat\xc3\xb3rio)'),
        ),
    ]
