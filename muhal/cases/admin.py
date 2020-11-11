from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

from modeltranslation.admin import TranslationTabularInline, TranslationAdmin, TabbedTranslationAdmin
from pagedown.widgets import AdminPagedownWidget

from .models import Case, Defendant, Plaintiff, LawArticle, Judge, Reference
from attachments.admin import AttachmentInline


class PlaintiffAdmin(TabbedTranslationAdmin):
    list_display = ['first_name', 'last_name', 'description']
    search_fields = ['first_name', 'last_name', 'description']


class DefendantAdmin(TabbedTranslationAdmin):
    list_display = ['first_name', 'last_name', 'gender',
                    'citizenship', 'profession', 'age_range', ]
    search_fields = ['first_name', 'last_name', ]


class LawArticleAdmin(TabbedTranslationAdmin):
    list_display = ['law', 'number', 'name', ]
    search_fields = ['number', 'name', ]
    list_filter = ['law', ]


class JudgeAdmin(TabbedTranslationAdmin):
    list_display = ['first_name', 'last_name', 'legal_entity', 'kaza', ]


class ReferenceInline(TranslationTabularInline):
    model = Reference
    extra = 1


class CaseAdmin(TabbedTranslationAdmin):
    fieldsets = (
        (_('Required basic information'), {
            'fields': ['country', 'summary', 'defendants', 'plaintiffs', 'platform', 'current_status', 'date_of_contact', 'date_of_publication'],
            'classes': ('collapse-open',),
        }),
        (_('Complaint details'), {
            'fields': ['date_of_investigation', 'station_name', 'detained', 'detained_for', 'pledge_signing',
                       'content_deletion', 'reconciliation', 'contacted_via', ],
            'classes': ('collapse-closed',),
        }),
        (_('Lawsuit details'), {
            'fields': ['judges', 'charge', 'charged_using', 'bail', 'sentenced', 'sentence', 'in_absentia', ],
            'classes': ('collapse-closed',)
        }),
        (_('Timeline'), {
            'fields': ['date_of_detention',  # 'date_of_contact', 'date_of_investigation', 'date_of_publication'
                        'date_of_hearing',  'date_of_hearing_2', # 'duration_of_detention',
                       'date_of_release', 'date_of_ruling', ],
            'classes': ('collapse-closed',)
        }),
        (_('Publishing'), {
            'fields': ['published', 'created', 'last_modified'],
        }),
    )
    readonly_fields = ('created', 'last_modified')

    list_display = ['__str__', 'platform', 'current_status',
                    'date_of_publication', 'date_of_contact', 'plaintiffs_list', 'defendants_list', 'published', 'last_modified']
    search_fields = ['summary', ]
    list_filter = ['current_status', 'platform', 'published', 'plaintiffs',]
    filter_horizontal = ('plaintiffs', 'defendants', 'charged_using', 'judges')
    inlines = (ReferenceInline, AttachmentInline, )
    list_display_links = ['__str__', ]
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }


admin.site.register(Plaintiff, PlaintiffAdmin)
admin.site.register(Defendant, DefendantAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(LawArticle, LawArticleAdmin)
admin.site.register(Judge, JudgeAdmin)
