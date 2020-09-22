from rest_framework import serializers

from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['submitter', 'country', 'plaintiff', 'defendant', 'what_happened']
