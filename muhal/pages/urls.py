from django.conf.urls import include
from django.urls import path

from rest_framework import routers

from .views import PagesViewSet

router = routers.DefaultRouter()
router.register(r'pages', PagesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]