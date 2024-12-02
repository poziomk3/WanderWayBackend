from django.urls import path, include
from WanderWayBackend.views.test.views import GetAllPOIs, GetPOI

urlpatterns = [
    path('poi', GetAllPOIs.as_view(), name='get_pois'),
    path('poi/<int:poi_id>/', GetPOI.as_view(), name='get_poi'),

]