from django.db import models


class POI(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    imgURI = models.CharField(default=None, blank=True, null=True, max_length=100)

    def __str__(self):
        return self.id