from django.urls import path
from django.conf.urls import include, url
from api.views import GhostPostViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'ghostpost', GhostPostViewSet, basename='ghostpost')

urlpatterns = [
    url(r"api/", include(router.urls))
]