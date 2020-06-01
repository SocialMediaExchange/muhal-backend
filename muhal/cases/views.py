from rest_framework import viewsets

from .models import Case
from .serializers import CaseSerializer

# ViewSets define the view behavior.
class CaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Case.objects.all() #FIXME create a queryset manager for published()
    serializer_class = CaseSerializer