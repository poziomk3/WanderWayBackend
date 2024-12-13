from django.contrib.auth.models import User  # Import the default User model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class ForumPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference the built-in User model
    created_at = models.DateTimeField(auto_now_add=True)
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
