from django.contrib import admin

from shop.models import ProductImage, Product, Category, Subcategory
from sorl.thumbnail.admin import AdminImageMixin

class ProductImageAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['image_title']
    search_fields = ['image_title']

class ProductImageInline(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    
    list_display = ['name', 'added', 'product_id', 'in_stock', 'description', 'subcategory', 'category']
    list_filter = ['added']
    search_fields = ['product_id', 'name', 'description', 'in_stock']

    prepopulated_fields = {"slug": ('product_id',)}

    inlines = [ProductImageInline,]

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)  
  
    list_display = ['name', 'added']
    list_filter = ['added']  
    search_fields = ['name']
    date_hierarchy = 'added'
  
    prepopulated_fields = {"slug": ('name',)}
    
class SubcategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)  
  
    list_display = ['name', 'added']
    list_filter = ['added']  
    search_fields = ['name']
    date_hierarchy = 'added'
  
    prepopulated_fields = {"slug": ('name',)}
  
  
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product, ProductAdmin)