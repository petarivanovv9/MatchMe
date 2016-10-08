# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True, default='')),
                ('start_time', models.DateTimeField(blank=True, default=datetime.datetime(2015, 11, 15, 16, 22, 2, 462733))),
                ('end_time', models.DateTimeField(blank=True, default=datetime.datetime(2015, 11, 15, 16, 22, 2, 462756))),
                ('description', models.CharField(blank=True, max_length=2500, null=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True, default='')),
                ('longitude', models.FloatField(blank=True, null=True, default=0.0)),
                ('latitude', models.FloatField(blank=True, null=True, default=0.0)),
                ('city', models.ForeignKey(to='website.City', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.ForeignKey(to='website.Place', null=True),
        ),
    ]
