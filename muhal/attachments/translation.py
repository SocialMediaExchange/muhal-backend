from modeltranslation.translator import translator, TranslationOptions
from .models import Attachment


class AttachmentTranslationOptions(TranslationOptions):
    fields = ('label', )


translator.register(Attachment, AttachmentTranslationOptions)
