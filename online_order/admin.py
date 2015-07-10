from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm, UserCreationForm
from django.utils.translation import ugettext, ugettext_lazy as _

from online_order.models import SparmedUser
# Register your models here.

class SparmedUserChangeForm(UserChangeForm):
    class Meta:
        model = SparmedUser
        fields = '__all__'
  
    def __init__(self, *args, **kwargs):
        super(SparmedUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['name'].required = True
      
class SparmedUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = SparmedUserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name', 'company_name', 'email', 'contact_person_name', 'is_admin', 'country',)
    list_filter = ('is_admin', 'country',)
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}),
        (_('Personal info'), {'fields': ('company_name', 'country', 'address', 'city', 'postal_code', 'contact_person_name', 'contact_telephone',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_admin', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'company_name', 'country', 'address', 'city', 'postal_code', 'contact_person_name', 'contact_telephone')}
        ),
    )
    
    search_fields = ('name', 'company_name', 'country', 'email', 'contact_person_name', 'address')
    ordering = ('company_name', 'country', 'name',)
    filter_horizontal = () 
    
admin.site.register(SparmedUser, SparmedUserAdmin)
#admin.site.unregister(Group)

#from django.contrib.auth.models import Permission
#admin.site.register(Permission)