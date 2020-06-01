from rest_framework import serializers

from .models import Case, Plaintiff, Defendant, Judge, LawArticle


class DefendantSerializer(serializers.ModelSerializer):
    citizenship = serializers.SerializerMethodField()

    class Meta:
        model = Defendant
        fields = ['first_name', 'last_name', 'gender',
                  'age_range', 'citizenship', 'profession']

    def get_citizenship(self, obj):
        return obj.get_citizenship_display()


class PlaintiffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plaintiff
        fields = ['first_name', 'last_name', ]


class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = '__all__'


class LawArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawArticle
        fields = '__all__'


class CaseSerializer(serializers.ModelSerializer):
    defendants = DefendantSerializer(required=False, many=True)
    plaintiffs = PlaintiffSerializer(required=False, many=True)
    judge = JudgeSerializer(required=False)
    charged_using = LawArticleSerializer(required=False, many=True)
    platform = serializers.SerializerMethodField()

    class Meta:
        model = Case
        fields = ['summary', 'defendants', 'plaintiffs', 'platform', 'current_status',

                  'charge', 'charged_using', 'bail',

                  'judge', 'sentenced', 'sentence', 'in_absentia', 'detained', 'detained_for',
                  'pledge_signing', 'content_deletion', 'contacted_via',

                  'date_of_publication', 'date_of_contact', 'date_of_investigation', 'date_of_detention',
                  'duration_of_detention', 'date_of_hearing', 'date_of_hearing_2',
                  'date_of_release', 'date_of_ruling',
                  ]

    def get_platform(self, obj):
        return obj.get_platform_display()
