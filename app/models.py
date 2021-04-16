from django.db import models
from django.contrib.gis.db import models as gis_models


class Country(models.Model):
    name = models.CharField(max_length=200)
    location = gis_models.PolygonField(null=True)

    def __str__(self):
        return self.name