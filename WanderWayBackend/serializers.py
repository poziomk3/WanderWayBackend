from rest_framework import serializers

from WanderWayBackend.models.forum_post_model import ForumPost
from WanderWayBackend.models.poi_model import POI

class POISerializer(serializers.ModelSerializer):
    class Meta:
        model = POI
        fields = ['id', 'name', 'description', 'latitude', 'longitude']

class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = ['id', 'title', 'body', 'author', 'date_posted']