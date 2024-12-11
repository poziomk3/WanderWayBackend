from requests import Response
from rest_framework.views import APIView


class getPosts(APIView):
    def get(self, request):
        return Response()

class createPost(APIView):
    def post(self, request, route_id):
        return Response()