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
        (_("Case details"), {
            "fields": ["name", "date", "summary", "defendants", "plaintiffs", "platform", "current_status", ],
        }),
        (_("Expression of opinion"), {
            "fields": ["charge", "charged_using", "bail", ],
        }),
        (_("Publishing"), {
            "fields": ["status", ("publish_date", "expiry_date")],
        }),
        (_("Meta data"), {
            "fields": ["_meta_title", "slug",
                       ("description", "gen_description"),
                        "keywords", "in_sitemap"],
            "classes": ("collapse-closed",)
        }),
    )

    list_display = ['title', 'status', 'date', ]
    search_fields = ['name', 'summary']
    filter_horizontal = ('plaintiffs', 'defendants', 'charged_using', )

admin.site.register(Plaintiff, PlaintiffAdmin)
admin.site.register(Defendant, DefendantAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(LawArticle, LawArticleAdmin)