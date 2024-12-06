from django.db import models


class Route(models.Model):
    id = models.AutoField(primary_key=True)
    filePath = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    imgURI = models.CharField(default=None, blank=True, null=True, max_length=100)