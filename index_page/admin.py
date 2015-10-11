from django.contrib import admin

# Register your models here.
from index_page.models import IndexPageModel

class IndexPageModelAdmin(admin.ModelAdmin):
    list_display = ['slogan']

admin.site.register(IndexPageModel, IndexPageModelAdmin)