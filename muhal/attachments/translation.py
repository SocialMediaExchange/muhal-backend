from modeltranslation.translator import translator, TranslationOptions
from .models import Attachment
from mezzanine.core.translation import TranslatedDisplayable

class AttachmentTranslationOptions(TranslationOptions):
    fields = ('label', )


translator.register(Attachment, AttachmentTranslationOptions)