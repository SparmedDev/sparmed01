from modeltranslation.translator import register, TranslationOptions
from index_page.models import IndexPageModel

@register(IndexPageModel)
class IndexPageTranslationOptions(TranslationOptions):
    fields = ('slogan',)