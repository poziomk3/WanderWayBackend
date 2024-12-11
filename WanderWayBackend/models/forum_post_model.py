from django.db import models

class ForumPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    route_id = models.ForeignKey('Route', on_delete=models.CASCADE)