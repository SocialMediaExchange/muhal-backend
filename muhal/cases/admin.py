from django.contrib import admin
from mezzanine.pages.admin import DisplayableAdmin
from mezzanine.core.admin import BaseTranslationModelAdmin
from .models import Case, Accused

class AccusedAdmin(BaseTranslationModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'citizenship', 'profession', 'age_range', ]
    search_fields = ['first_name', 'last_name', ]

admin.site.register(Accused, AccusedAdmin)
admin.site.register(Case, DisplayableAdmin)