from rest_framework import viewsets
from rest_framework.response import Response

from .models import Case, Plaintiff, PLATFORM_CHOICES
from .serializers import CaseSerializer, PlaintiffSerializer


class CaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Case.objects.filter(published=True).order_by('-date_of_contact')
    serializer_class = CaseSerializer


class PlaintiffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Plaintiff.objects.all().order_by('last_name')
    serializer_class = PlaintiffSerializer


class PlatformOptionsViewSet(viewsets.ViewSet):
    def list(self, request):
        options = PLATFORM_CHOICES
        return Response(options)
