from django.contrib import admin
from distributors.models import Distributor

# Register your models here.
class DistributorAdmin(admin.ModelAdmin):
    list_display = ['country', 'latitude', 'longitude']
    search_fields = ['country']
    
admin.site.register(Distributor, DistributorAdmin)