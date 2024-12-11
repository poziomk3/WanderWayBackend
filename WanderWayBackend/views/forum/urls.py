from django.urls import path
from WanderWayBackend.views.forum.views import *

urlpatterns = [
    path('getPosts/' , getPosts.as_view(), name='get_posts'),
]