from modeltranslation.translator import translator, TranslationOptions
from .models import Case, Plaintiff, Defendant
from mezzanine.core.translation import TranslatedDisplayable

class CaseTranslationOptions(TranslatedDisplayable):
    fields = ('name', 'summary', )

class DefendantTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'profession')

class PlaintiffTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', )

translator.register(Defendant, DefendantTranslationOptions)
translator.register(Plaintiff, PlaintiffTranslationOptions)
translator.register(Case, CaseTranslationOptions)