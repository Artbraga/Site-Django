# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('atributo', models.CharField(max_length=20, verbose_name=b'M\xc3\xaas')),
                ('valor', models.CharField(max_length=50, verbose_name=b'M\xc3\xaas')),
            ],
        ),
    ]
