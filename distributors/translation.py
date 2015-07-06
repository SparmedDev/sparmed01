from modeltranslation.translator import register, TranslationOptions
from distributors.models import Distributor

@register(Distributor)
class DistributorTranslationOptions(TranslationOptions):
    fields = ('country',)