import os.path
from django.http import FileResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from WanderWayBackend.models.poi_model import POI
from WanderWayBackend.serializers import POISerializer
from WanderWayBackend.views.route.lib import *


class GetAllPOIs(APIView):
    """
        get:
        Return a list of all POIs.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: openapi.Schema(
                title="POIs",
                type=openapi.TYPE_OBJECT,
                properties={
                    "pois": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                "name": openapi.Schema(type=openapi.TYPE_STRING),
                                "description": openapi.Schema(type=openapi.TYPE_STRING),
                                "latitude": openapi.Schema(type=openapi.TYPE_NUMBER),
                                "longitude": openapi.Schema(type=openapi.TYPE_NUMBER),
                            },
                        ),
                    ),
                },
            )
        },
    )
    def get(self, request):
        pois = POI.objects.all()
        serializer = POISerializer(pois, many=True)
        return Response({'pois': serializer.data})


class GetPOI(APIView):
    """
        get:
        Return a POI by its ID.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: openapi.Schema(
                title="POI",
                type=openapi.TYPE_OBJECT,
                properties={
                    "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                    "name": openapi.Schema(type=openapi.TYPE_STRING),
                    "description": openapi.Schema(type=openapi.TYPE_STRING),
                    "latitude": openapi.Schema(type=openapi.TYPE_NUMBER),
                    "longitude": openapi.Schema(type=openapi.TYPE_NUMBER),
                },
            ),
            status.HTTP_404_NOT_FOUND: openapi.Schema(
                title="Error",
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        },
    )
    def get(self, request, poi_id):
        try:
            poi = POI.objects.get(id=poi_id)
            serializer = POISerializer(poi)
            return Response(serializer.data)
        except POI.DoesNotExist:
            return Response({'error': 'POI not found'}, status=404)


class GetPOIImg(APIView):
    """
        get:
        Return a POI image by the POI's ID.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Image file",
                content={'image/jpeg': {}},
                schema=openapi.Schema(type=openapi.TYPE_FILE),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Schema(
                title="Error",
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        },
    )
    def get(self, request, poi_id):
        img_file, filename, op_status = get_poi_img(poi_id)
        if not img_file:
            return Response({'error': op_status}, status=404)

        return FileResponse(
            img_file,
            as_attachment=False,
            filename=filename,
            content_type='image/jpeg'
        )


class GenRoutes(APIView):
    """
        post:
        Generate routes based on provided POIs and preferences.
        At this time the content of both 'pois' and 'preferences' is ignored.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'pois': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_INTEGER),
                ),
                'preferences': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={},
                ),
            },
        ),
        responses={
            status.HTTP_200_OK: openapi.Schema(
                title="Route IDs",
                type=openapi.TYPE_OBJECT,
                properties={
                    "routeIds": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_INTEGER),
                    ),
                },
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Schema(
                title="Error",
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        },
    )
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

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Route file",
                content={'application/gpx+xml': {}},
                schema = openapi.Schema(type=openapi.TYPE_FILE),
            ),
            status.HTTP_404_NOT_FOUND: openapi.Schema(
                title="Error",
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        },
    )
    def get(self, request, route_id):
        route, op_status = get_route_obj(route_id)
        if not route:
            return Response({'error': op_status}, status=404)

        file, filename, op_status = get_route_file(route)
        if not file:
            return Response({'error': op_status}, status=404)

        return FileResponse(
            file,
            as_attachment=False,
            filename=filename,
            content_type='application/gpx+xml'
        )


class GetRouteImg(APIView):
    """
        get:
        Return a Route image by the route's ID.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'imgtype',
                openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                enum=['roadmap', 'satellite', 'hybrid', 'terrain'],
                default='roadmap',
                description='Type of image to return',
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Image file",
                content={'image/jpeg': {}},
                schema=openapi.Schema(type=openapi.TYPE_FILE),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Schema(
                title="Error",
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
            status.HTTP_404_NOT_FOUND: openapi.Schema(
                title="Error",
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        },
    )
    def get(self, request, route_id):
        img_type = request.GET.get('imgtype', 'roadmap')
        if img_type not in ['roadmap', 'satellite', 'hybrid', 'terrain']:
            return Response({'error': 'Invalid image type'}, status=400)

        route_img, filename, op_status = get_route_img(route_id, img_type)
        if not route_img:
            return Response({'error': op_status}, status=404)

        return FileResponse(
            route_img,
            as_attachment=False,
            filename=filename,
            content_type='image/jpeg'
        )
