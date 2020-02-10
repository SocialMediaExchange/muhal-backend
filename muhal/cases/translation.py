from modeltranslation.translator import translator, TranslationOptions
from .models import Case, Accused
from mezzanine.core.translation import TranslatedDisplayable

class CaseTranslationOptions(TranslatedDisplayable):
    fields = ('name', )

class AccusedTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', )


translator.register(Accused, AccusedTranslationOptions)
translator.register(Case, CaseTranslationOptions)