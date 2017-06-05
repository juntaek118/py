# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webtoon',
            name='List',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='webtoon',
            name='New',
            field=models.CharField(max_length=50),
        ),
    ]
