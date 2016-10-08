# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0002_auto_20151115_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 15, 19, 16, 46, 552196), blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 15, 19, 16, 46, 552175), blank=True),
        ),
        migrations.AddField(
            model_name='eventuser',
            name='event',
            field=models.ForeignKey(to='website.Event'),
        ),
        migrations.AddField(
            model_name='eventuser',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
