from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Report


class ReportAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Submitted information'), {
            'fields': ['country', 'plaintiff', 'defendant', 'what_happened', ],
            'classes': ('collapse-open',),
        }),
        (_('Admin details'), {
            'fields': ['notes', 'created', 'last_modified', 'processed', ],
            'classes': ('collapse-open',),
        }),
    )
    list_display = ['country', 'plaintiff',
                    'defendant', 'created', 'processed']
    search_fields = ['what_happened', 'plaintiff', 'defendant']
    list_filter = ['processed', 'country']
    readonly_fields = ('country', 'plaintiff', 'defendant',
                       'what_happened', 'created', 'last_modified')


admin.site.register(Report, ReportAdmin)
