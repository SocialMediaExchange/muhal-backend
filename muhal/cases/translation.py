from modeltranslation.translator import translator, TranslationOptions
from .models import Case, Plaintiff, Defendant, LawArticle, Judge
from mezzanine.core.translation import TranslatedDisplayable

class CaseTranslationOptions(TranslatedDisplayable):
    fields = ('summary', )

class DefendantTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'profession')

class PlaintiffTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', )

class LawArticleTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(Defendant, DefendantTranslationOptions)
translator.register(Plaintiff, PlaintiffTranslationOptions)
translator.register(Case, CaseTranslationOptions)
translator.register(LawArticle, LawArticleTranslationOptions)
translator.register(Judge, PlaintiffTranslationOptions)
