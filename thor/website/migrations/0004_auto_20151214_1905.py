# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0003_auto_20151115_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('first_name', models.CharField(default='', null=True, blank=True, max_length=20)),
                ('last_name', models.CharField(default='', null=True, blank=True, max_length=20)),
                ('age', models.IntegerField(default=0, null=True, blank=True)),
                ('city', models.ForeignKey(to='website.City', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 14, 19, 5, 2, 470082), blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 14, 19, 5, 2, 470059), blank=True),
        ),
    ]
