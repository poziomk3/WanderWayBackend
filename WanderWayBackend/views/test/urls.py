from django.urls import path

from WanderWayBackend.views.test.views import SecuredTestView, TestView

urlpatterns = [
    path('secured', SecuredTestView.as_view(), name='secured_test'),
    path('unsecured', TestView.as_view(), name='unsecured_test'),
]