from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import Page


class PageAdmin(TabbedTranslationAdmin):
    pass


admin.site.register(Page, PageAdmin)
