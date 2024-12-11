from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from WanderWayBackend.models.forum_post_model import ForumPost
from WanderWayBackend.models.route_model import Route
from WanderWayBackend.serializers import ForumPostSerializer


class getPosts(APIView):
    """
        get:
        Return a list of all posts.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={200: ForumPostSerializer(many=True)}
    )
    def get(self, request):
        posts = ForumPost.objects.all()
        serializer = ForumPostSerializer(posts, many=True)
        return Response({'posts': serializer.data})


class Post(APIView):
    """
        post:
        Create a new forum post for a route specified with the id.

        get:
        Get a forum post by the post's id.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=ForumPostSerializer,
        responses={
            status.HTTP_201_CREATED: openapi.Schema(
                title="Forum Post ID",
                type=openapi.TYPE_OBJECT,
                properties={
                    "post_id": openapi.Schema(
                        type=openapi.TYPE_INTEGER,
                        example=1,
                    ),
                },
            ),
            status.HTTP_404_NOT_FOUND: openapi.Schema(
                title="Error",
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING, example="Route not found"),
                },
            ),
        },
    )
    def post(self, request, id):
        try:
            route = Route.objects.get(id=id)
            post = ForumPost.objects.create(
                title=request.data['title'],
                rating=request.data['rating'],
                body=request.data['body'],
                author=request.user,
                route=route,
            )
            return Response({"post_id": post.id}, status=201)
        except Route.DoesNotExist:
            return Response({"error": "Route not found"}, status=404)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: ForumPostSerializer,
            status.HTTP_404_NOT_FOUND: openapi.Schema(
                title="Error",
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING, example="Post not found"),
                },
            ),
        },
    )
    def get(self, request, id):
        try:
            post = ForumPost.objects.get(id=id)
            serializer = ForumPostSerializer(post)
            return Response(serializer.data)
        except ForumPost.DoesNotExist:
            return Response({"error": "Post not found"}, status=404)
