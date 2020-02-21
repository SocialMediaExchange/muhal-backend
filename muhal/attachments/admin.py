from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from modeltranslation.admin import TranslationGenericTabularInline

from .models import Attachment

class AttachmentInline(TranslationGenericTabularInline):
    model = Attachment
    extra = 1