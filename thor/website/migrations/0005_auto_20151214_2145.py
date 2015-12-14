# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20151214_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventuser',
            name='status',
            field=models.IntegerField(null=True, blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 12, 14, 21, 45, 58, 717885)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 12, 14, 21, 45, 58, 717864)),
        ),
    ]
