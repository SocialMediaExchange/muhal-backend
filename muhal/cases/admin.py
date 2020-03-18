from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from mezzanine.pages.admin import DisplayableAdmin
from mezzanine.core.admin import BaseTranslationModelAdmin
from modeltranslation.admin import TranslationTabularInline

from .models import Case, Defendant, Plaintiff, LawArticle, Judge, Reference
from attachments.admin import AttachmentInline

class PlaintiffAdmin(BaseTranslationModelAdmin):
    list_display = ['first_name', 'last_name', ]
    search_fields = ['first_name', 'last_name', ]

class DefendantAdmin(BaseTranslationModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'citizenship', 'profession', 'age_range', ]
    search_fields = ['first_name', 'last_name', ]

class LawArticleAdmin(BaseTranslationModelAdmin):
    list_display = ['law', 'number', 'name', ]
    search_fields = ['number', 'name', ]

class JudgeAdmin(BaseTranslationModelAdmin):
    list_display = ['first_name', 'last_name', 'legal_entity', 'kaza', ]

class ReferenceInline(TranslationTabularInline):
    model = Reference
    extra = 1

class CaseAdmin(DisplayableAdmin):
    fieldsets = (
        (_('Basic information'), {
            'fields': [#('country', ), 
                       'summary', 'defendants', 'plaintiffs', 'platform', 'current_status', ],
            'classes': ('collapse-open',),
        }),
        (_('Complaint details'), {
            'fields': ['date_of_contact', 'date_of_investigation', 'station_name', 'detained', 'detained_for', 'pledge_signing', 
                       'content_deletion', 'reconciliation', 'contacted_via', ],
            'classes': ('collapse-closed',),
        }),
        (_('Case details'), {
            'fields': ['judge', 'charge', 'charged_using', 'bail', 'sentenced', 'sentence', 'in_absentia', ],
            'classes': ('collapse-closed',)
        }),
        (_('Timeline'), {
            'fields': ['date_of_publication', 'date_of_contact', 'date_of_investigation', 'date_of_detention', 
                       'duration_of_detention', 'date_of_hearing',  'date_of_hearing_2', 
                       'date_of_release', 'date_of_ruling', ],
            'classes': ('collapse-closed',)
        }),
        (_('Publishing'), {
            'fields': ['status', ('publish_date', 'expiry_date')],
            'classes': ('collapse-closed',),
        }),
        (_('Meta data'), {
            'fields': ['_meta_title', 'slug',
                       ('description', 'gen_description'),
                        'keywords', 'in_sitemap'],
            'classes': ('collapse-closed',),
        }),
    )

    list_display = ['__str__', 'platform', 'current_status', 'date_of_publication', 'status',]
    search_fields = ['summary', ]
    list_filter = ['status', 'current_status', 'defendants', 'plaintiffs', ]
    filter_horizontal = ('plaintiffs', 'defendants', 'charged_using', )
    inlines = (ReferenceInline, AttachmentInline, )
    list_display_links = ['__str__', ]

admin.site.register(Plaintiff, PlaintiffAdmin)
admin.site.register(Defendant, DefendantAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(LawArticle, LawArticleAdmin)
admin.site.register(Judge, JudgeAdmin)