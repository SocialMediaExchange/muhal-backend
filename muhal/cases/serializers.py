from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import Case, Plaintiff, Defendant, Judge, LawArticle


class DefendantSerializer(serializers.ModelSerializer):
    citizenship = serializers.SerializerMethodField()

    class Meta:
        model = Defendant
        fields = ['id', 'first_name', 'last_name', 'gender',
                  'age_range', 'citizenship', 'profession']

    def get_citizenship(self, obj):
        return obj.get_citizenship_display()


class PlaintiffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plaintiff
        fields = ['id', 'first_name', 'last_name', ]


class JudgeSerializer(serializers.ModelSerializer):
    legal_entity = serializers.SerializerMethodField()
    kaza = serializers.SerializerMethodField()

    class Meta:
        model = Judge
        fields = ['id', 'first_name', 'last_name', 'legal_entity', 'kaza']

    def get_legal_entity(self, obj):
        return obj.get_legal_entity_display()

    def get_kaza(self, obj):
        return obj.get_kaza_display()


class LawArticleSerializer(serializers.ModelSerializer):
    law = serializers.SerializerMethodField()

    class Meta:
        model = LawArticle
        fields = ['id', 'law', 'number', 'name', 'url', ]

    def get_law(self, obj):
        return obj.get_law_display()


class CaseSerializer(serializers.ModelSerializer):
    defendants = DefendantSerializer(required=False, many=True)
    plaintiffs = PlaintiffSerializer(required=False, many=True)
    judges = JudgeSerializer(required=False, many=True)
    charged_using = LawArticleSerializer(required=False, many=True)
    platform_display = serializers.SerializerMethodField()
    detained = serializers.SerializerMethodField()
    content_deletion = serializers.SerializerMethodField()
    pledge_signing = serializers.SerializerMethodField()
    reconciliation = serializers.SerializerMethodField()
    contacted_via = serializers.SerializerMethodField()
    sentenced = serializers.SerializerMethodField()
    in_absentia = serializers.SerializerMethodField()

    class Meta:
        model = Case
        fields = ['id', 'summary', 'defendants', 'plaintiffs', 'platform', 'platform_display', 'current_status',

                  'charge', 'charged_using', 'bail',

                  'station_name', 'detained', 'detained_for',  'content_deletion', 'pledge_signing', 'reconciliation', 'contacted_via',
                  'judges', 'sentenced', 'sentence', 'in_absentia',

                  'date_of_publication', 'date_of_contact', 'date_of_investigation', 'date_of_detention',
                  'duration_of_detention', 'date_of_hearing', 'date_of_hearing_2',
                  'date_of_release', 'date_of_ruling',
                  ]

    def get_platform_display(self, obj):
        return obj.get_platform_display()

    def get_detained(self, obj):
        return obj.get_detained_display()

    def get_content_deletion(self, obj):
        return obj.get_content_deletion_display()

    def get_pledge_signing(self, obj):
        return obj.get_pledge_signing_display()

    def get_reconciliation(self, obj):
        if obj.reconciliation == None:
            return None
        else:
            return _('yes') if obj.reconciliation else _('no')

    def get_contacted_via(self, obj):
        return obj.get_contacted_via_display()

    def get_sentenced(self, obj):
        return obj.get_sentenced_display()

    def get_in_absentia(self, obj):
        return obj.get_in_absentia_display()
