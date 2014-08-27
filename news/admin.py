from django.contrib import admin
from news.models import NewsPost, NewsImage

# Register your models here.
class NewsImageAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['image_title']
    search_fields = ['image_title']

class NewsImageInline(admin.StackedInline):
    model = NewsImage 
    
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'added']
    list_filter = ['added']
    search_fields = ['title', 'content']
    date_hierarchy = 'added'
    
    preopulated_fields = {"slug": ('title',)}
    
    inlines = [NewsImageInline,]

admin.site.register(NewsImage, NewsImageAdmin)
admin.site.register(NewsPost, NewsPostAdmin)