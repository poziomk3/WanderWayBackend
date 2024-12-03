from django.db import models
from rest_framework.authtoken.admin import User


class Route(models.Model):
    id = models.AutoField(primary_key=True)
    filePath = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)