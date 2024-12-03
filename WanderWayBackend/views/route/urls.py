from django.urls import path
from WanderWayBackend.views.route.views import *


urlpatterns = [
    path('poi', GetAllPOIs.as_view(), name='get_pois'),
    path('poi/<int:poi_id>/', GetPOI.as_view(), name='get_poi'),
    path("generate", GenRoutes.as_view(), name='gen_routes'),
    path('<int:route_id>/', GetRoute.as_view(), name='get_route'),
]