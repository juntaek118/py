# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('webdata', '0002_auto_20170603_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='webtoon',
            name='Time',
            field=models.CharField(max_length=20, default=datetime.datetime(2017, 6, 3, 16, 42, 28, 676932, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='webtoon',
            name='Name',
            field=models.CharField(max_length=30),
        ),
    ]
