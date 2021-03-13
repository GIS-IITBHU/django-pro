from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=32644)
    objects = GeoManager()

    def unicode(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Incidences'


class Hostels(models.Model):
    name = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    hostelid = models.CharField(max_length=254)
    geom = models.MultiPolygonField(srid=32644)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Hostels'

