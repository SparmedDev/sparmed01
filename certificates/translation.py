from modeltranslation.translator import register, TranslationOptions
from certificates.models import CertificateItem,CertificateSubgroup,CertificateGroup

@register(CertificateItem)
class CertificateItemTranslationOptions(TranslationOptions):
    fields = ('title',)
    
@register(CertificateSubgroup)
class CertificateSubgroupTranslationOptions(TranslationOptions):
  fields = ('title',)
  
@register(CertificateGroup)
class CertificateGroupTranslationOptions(TranslationOptions):
    fields = ('title',)