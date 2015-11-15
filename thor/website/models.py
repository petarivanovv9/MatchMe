from django.db import models

from datetime import datetime

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=20, blank=True, default="", null=True)

    def __str__(self):
        return "{}".format(self.name)


class Place(models.Model):
    city = models.ForeignKey(City, null=True)
    name = models.CharField(max_length=100, blank=True, default="", null=True)
    longitude = models.FloatField(blank=True, default=0.0, null=True)
    latitude = models.FloatField(blank=True, default=0.0, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Event(models.Model):
    name = models.CharField(max_length=100, blank=True, default="", null=True)
    start_time = models.DateTimeField(default=datetime.now(), blank=True)
    end_time = models.DateTimeField(default=datetime.now(), blank=True)
    description = models.CharField(
        max_length=2500, blank=True, default="", null=True)

    place = models.ForeignKey(Place, null=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.place.name)
