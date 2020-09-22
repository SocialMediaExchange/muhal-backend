from rest_framework import viewsets, mixins

from .models import Report
from .serializers import ReportSerializer


class ReportCreateViewSet(mixins.CreateModelMixin,
                          viewsets.GenericViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
