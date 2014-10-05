from django.contrib import admin

from certificates.models import CertificateItem, CertificateSubgroup, CertificateGroup
# Register your models here.

class CertificateItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'added', 'order_index', 'subgroup', 'group']
    list_filter = ['added']
    search_fields = ['title', 'added', 'subgroup', 'group']
    
class CertificateSubgroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'added', 'group']
    list_filter = ['added']
    search_fields = ['title', 'added', 'group']
    
class CertificateGroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'added']
    list_filter = ['added']
    search_fields = ['title', 'added']
    
admin.site.register(CertificateItem, CertificateItemAdmin)
admin.site.register(CertificateSubgroup, CertificateSubgroupAdmin)
admin.site.register(CertificateGroup, CertificateGroupAdmin)