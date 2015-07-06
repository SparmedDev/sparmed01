from modeltranslation.translator import register, TranslationOptions
from news.models import NewsImage, NewsPost

@register(NewsImage)
class NewsImageTranslationOptions(TranslationOptions):
    fields = ('image_title',)
    
@register(NewsPost)
class NewsPostTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)