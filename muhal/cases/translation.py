from modeltranslation.translator import translator, TranslationOptions
from .models import Case, Plaintiff, Defendant, LawArticle, Judge, Reference

class CaseTranslationOptions(TranslationOptions):
    fields = ('summary', )

class DefendantTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'profession')

class PlaintiffTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', )

class LawArticleTranslationOptions(TranslationOptions):
    fields = ('name', )

class ReferenceTranslationOptions(TranslationOptions):
    fields = ('title', )


translator.register(Defendant, DefendantTranslationOptions)
translator.register(Plaintiff, PlaintiffTranslationOptions)
translator.register(Case, CaseTranslationOptions)
translator.register(LawArticle, LawArticleTranslationOptions)
translator.register(Judge, PlaintiffTranslationOptions)
translator.register(Reference, ReferenceTranslationOptions)
