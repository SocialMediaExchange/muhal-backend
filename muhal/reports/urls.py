from django.conf.urls import include
from django.urls import path

from rest_framework import routers

from .views import ReportCreateViewSet

router = routers.DefaultRouter()
router.register(r'reports', ReportCreateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]