from rest_framework import viewsets
from rest_framework.response import Response

from .models import Case, Plaintiff, PLATFORM_CHOICES
from .serializers import CaseSerializer, PlaintiffSerializer

# ViewSets define the view behavior.


class CaseViewSet(viewsets.ReadOnlyModelViewSet):
    # FIXME create a queryset manager for published()
    queryset = Case.objects.all().order_by('-date_of_contact')
    serializer_class = CaseSerializer


class PlaintiffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Plaintiff.objects.all().order_by('last_name')
    serializer_class = PlaintiffSerializer


class PlatformOptionsViewSet(viewsets.ViewSet):
    def list(self, request):
        options = PLATFORM_CHOICES
        return Response(options)
