from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from WanderWayBackend.models.forum_post_model import ForumPost
from WanderWayBackend.serializers import ForumPostSerializer


class getPosts(APIView):
    """
        get:
        Return a list of all posts.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = ForumPost.objects.all()
        serializer = ForumPostSerializer(posts, many=True)
        return Response({'posts': serializer.data})


class createPost(APIView):
    """
        post:
        Create a new post.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, route_id):
        post = ForumPost.objects.create(
            title=request.data['title'],
            rating=request.data['rating'],
            body=request.data['body'],
            author=request.user,
            route_id=route_id,
        )
        return Response({"post_id": post.id}, status=201)