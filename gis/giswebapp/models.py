from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = GeoManager()

    def unicode(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Incidences'