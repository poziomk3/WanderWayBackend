from rest_framework import serializers

from WanderWayBackend.models.forum_post_model import ForumPost
from WanderWayBackend.models.poi_model import POI

class POISerializer(serializers.ModelSerializer):
    class Meta:
        model = POI
        fields = ['id', 'name', 'description', 'latitude', 'longitude']

class ForumPostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = ForumPost
        fields = ['id', 'title', 'rating', 'body', 'author', 'created_at', 'route_id', 'img_url']
