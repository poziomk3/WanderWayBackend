from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from WanderWayBackend.models.poi_model import POI
from WanderWayBackend.models.route_model import Route
from WanderWayBackend.serializers import POISerializer


class GetAllPOIs(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        pois = POI.objects.all()
        serializer = POISerializer(pois, many=True)
        return Response({'pois': serializer.data})

class GetPOI(APIView):
    permission_classes = [AllowAny]
    def get(self, request, poi_id):
        try:
            poi = POI.objects.get(id=poi_id)
            serializer = POISerializer(poi)
            return Response(serializer.data)
        except POI.DoesNotExist:
            return Response({'error': 'POI not found'}, status=404)

class GenRoutes(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        pois = request.data.get('pois')
        if not pois:
            return Response({'error': 'No POIs provided'}, status=400)
        prefs = request.data.get('preferences')
        if not prefs:
            return Response({'error': 'No preferences provided'}, status=400)

        route_ids = Route.objects.all().values_list('id', flat=True)
        return Response({'routeIds': route_ids})