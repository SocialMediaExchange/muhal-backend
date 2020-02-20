from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from mezzanine.pages.admin import DisplayableAdmin
from mezzanine.core.admin import BaseTranslationModelAdmin

from .models import Case, Defendant, Plaintiff, LawArticle

class PlaintiffAdmin(BaseTranslationModelAdmin):
    list_display = ['first_name', 'last_name', ]
    search_fields = ['first_name', 'last_name', ]

class DefendantAdmin(BaseTranslationModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'citizenship', 'profession', 'age_range', ]
    search_fields = ['first_name', 'last_name', ]

class LawArticleAdmin(BaseTranslationModelAdmin):
    list_display = ['number', 'name', ]
    search_fields = ['number', 'name', ]

class CaseAdmin(DisplayableAdmin):
    fieldsets = (
        (_("Country"), {
            "fields": ["country", ],
        }),
        (_("Case details"), {
            "fields": ["date", "summary", "defendants", "plaintiffs", "platform", "current_status", ],
        }),
        (_("Expression of opinion"), {
            "fields": ["charge", "charged_using", "bail", ],
            "classes": ("collapse-closed",),
        }),
        (_("Investigation and detention"), {
            "fields": ["sentence", "sentenced", "in_absentia", "detained", "detained_for", "pledge_signing", "content_deletion", "contacted_via", ],
            "classes": ("collapse-closed",)
        }),
        (_("Publishing"), {
            "fields": ["status", ("publish_date", "expiry_date")],
            "classes": ("collapse-closed",)
        }),
        (_("Meta data"), {
            "fields": ["_meta_title", "slug",
                       ("description", "gen_description"),
                        "keywords", "in_sitemap"],
            "classes": ("collapse-closed",)
        }),
    )

    list_display = ['title', 'platform', 'current_status', 'date', 'status',]
    search_fields = ['summary', ]
    list_filter = ['status', 'current_status', 'defendants', 'plaintiffs', ]
    filter_horizontal = ('plaintiffs', 'defendants', 'charged_using', )

admin.site.register(Plaintiff, PlaintiffAdmin)
admin.site.register(Defendant, DefendantAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(LawArticle, LawArticleAdmin)