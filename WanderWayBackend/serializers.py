import random
from rest_framework import serializers
from rest_framework import request

from WanderWayBackend.lib import get_route_pois
from WanderWayBackend.models.forum_post_model import ForumPost
from WanderWayBackend.models.poi_model import POI


class POISerializer(serializers.ModelSerializer):
    class Meta:
        model = POI
        fields = ['id', 'name', 'description', 'latitude', 'longitude']


class ForumPostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    random_poi_id = serializers.SerializerMethodField()  # Use SerializerMethodField

    def get_random_poi_id(self, obj):

        pois, status = get_route_pois(obj.route)
        if not pois:
            return 1
        return random.choice(pois).id

    class Meta:
        model = ForumPost
        fields = ['id', 'title', 'rating', 'body', 'author', 'created_at', 'route', 'random_poi_id']
