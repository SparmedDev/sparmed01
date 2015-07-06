from modeltranslation.translator import register, TranslationOptions
from shop.models import ProductImage, ShopImage, Product, Subcategory, Category

@register(ProductImage)
class ProductImageTranslationOptions(TranslationOptions):
    fields = ('image_title',)
    
@register(ShopImage)
class ShopImageTranslationOptions(TranslationOptions):
    fields = ('image_title',)    
    
@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'long_name', 'description', 'long_text',)
    
@register(Subcategory)
class SubcategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'long_text',)
    
@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'short_name', 'description', 'long_text',)    