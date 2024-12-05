from rest_framework import serializers
from WanderWayBackend.models.poi_model import POI

class POISerializer(serializers.ModelSerializer):
    class Meta:
        model = POI
        fields = ['id', 'name', 'description', 'latitude', 'longitude']