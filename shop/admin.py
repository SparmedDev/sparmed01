from django.contrib import admin

from shop.models import ProductImage, Product, Category, Subcategory
from sorl.thumbnail.admin import AdminImageMixin

class ProductImageAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['image_title']
    search_fields = ['image_title']

class ProductImageInline(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'added', 'product_id', 'in_stock', 'description', 'subcategory', 'category']
    list_filter = ['added']
    search_fields = ['product_id', 'name', 'description', 'in_stock']

    prepopulated_fields = {"slug": ('product_id',)}

    inlines = [ProductImageInline,]
    
class SubcategoryAdmin(admin.ModelAdmin):
    change_form_template = 'shop/admin/change_form.html'
    
    list_display = ['name', 'added']
    list_filter = ['added']  
    search_fields = ['name']
    date_hierarchy = 'added'
  
    prepopulated_fields = {"slug": ('name',)}
  
class CategoryAdmin(admin.ModelAdmin):
    change_form_template = 'shop/admin/change_form.html'
  
    list_display = ['name', 'added']
    list_filter = ['added']  
    search_fields = ['name']
    date_hierarchy = 'added'
  
    prepopulated_fields = {"slug": ('short_name',)}
  
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product, ProductAdmin)