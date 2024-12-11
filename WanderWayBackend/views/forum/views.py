from requests import Response
from rest_framework.views import APIView


class getPosts(APIView):
    def get(self, request):
        # get all ForumPosts model objects