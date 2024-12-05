import os.path
from django.http import FileResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from WanderWayBackend.models.poi_model import POI
from WanderWayBackend.models.route_model import Route
from WanderWayBackend.serializers import POISerializer
from WanderWayBackend.settings import BASE_DIR


class GetAllPOIs(APIView):
    """
        get:
        Return a list of all POIs.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        pois = POI.objects.all()
        serializer = POISerializer(pois, many=True)
        return Response({'pois': serializer.data})


class GetPOI(APIView):
    """
        get:
        Return a POI by its ID.
    """
    permission_classes = [AllowAny]

    def get(self, request, poi_id):
        try:
            poi = POI.objects.get(id=poi_id)
            serializer = POISerializer(poi)
            return Response(serializer.data)
        except POI.DoesNotExist:
            return Response({'error': 'POI not found'}, status=404)


class GenRoutes(APIView):
    """
        post:
        Generate routes based on provided POIs and preferences.
    """
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


class GetRoute(APIView):
    """
        get:
        Return a route by its ID.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, route_id):
        if not route_id:
            return Response({'error': 'No route ID provided'}, status=400)
        try:
            route = Route.objects.get(id=route_id)
            file_name = route.filePath
            file_path = os.path.join(BASE_DIR, 'gpx', file_name)
            try:
                route_file = open(file_path, 'rb')  # Open in binary mode
                return FileResponse(
                    route_file,
                    as_attachment=True,
                    filename=file_name,
                    content_type='application/gpx+xml'
                )
            except FileNotFoundError:
                return Response({'error': 'File not found on server'}, status=404)
        except Route.DoesNotExist:
            return Response({'error': 'Route not found'}, status=404)
