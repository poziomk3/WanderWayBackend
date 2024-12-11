from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from WanderWayBackend.views.test.views import TestView

schema_view = get_schema_view(
    openapi.Info(
        title="WanderWay API",
        default_version='v1',
        description="API Documentation for WanderWay",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/test/',include('WanderWayBackend.views.test.urls'), name='test'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('auth/', include('WanderWayBackend.views.auth.urls')),
    path('route/', include('WanderWayBackend.views.route.urls')),
    path('forum/', include('WanderWayBackend.views.forum.urls')),
]
