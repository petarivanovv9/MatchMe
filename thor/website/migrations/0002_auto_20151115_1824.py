# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 11, 15, 18, 24, 1, 174364)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 11, 15, 18, 24, 1, 174343)),
        ),
    ]
