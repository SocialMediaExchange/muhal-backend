from rest_framework import viewsets, mixins, generics

from .models import Page
from .serializers import PageSerializer

class PagesViewSet(viewsets.GenericViewSet,
                             mixins.RetrieveModelMixin):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
