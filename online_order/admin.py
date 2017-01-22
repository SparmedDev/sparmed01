from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, PasswordResetForm, UserCreationForm, UserChangeForm
from django.utils.translation import ugettext, ugettext_lazy as _

from online_order.models import SparmedUser

class SparmedUserChangeForm(UserChangeForm):
    class Meta:
      model = SparmedUser
      fields = '__all__'

class SparmedUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = SparmedUserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name', 'company_name', 'email', 'contact_person_name', 'is_admin', 'is_staff', 'country', 'orders')
    list_filter = ('is_admin', 'country',)

    exclude = ('first_name', 'last_name',)

    fieldsets = (
        (_('Basic Info'), {
            'fields': ('name', 'email',),
        }),
        (_('Password'), {
            'fields': ('password',),
        }),
        (_('Personal Info'), {
            'fields': ('company_name', 'country', 'address', 'city', 'postal_code', 'contact_person_name', 'contact_telephone',)
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser', 'groups', 'user_permissions',)
        }),
        (_('Dates'), {
            'fields': ('last_login', 'date_joined',)
        }),
        (_('Orders'), {
            'fields': ('orders', ) 
        }),
    )

    add_fieldsets = (
        (_('Basic Info'), {
            'fields': ('name', 'email',),
        }),
        (_('Password'), {
            'fields': ('password1', 'password2',),
        }),
        (_('Personal Info'), {
            'fields': ('company_name', 'country', 'address', 'city', 'postal_code', 'contact_person_name', 'contact_telephone',)
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser', 'groups', 'user_permissions',)
        }),
        (_('Dates'), {
            'fields': ('last_login', 'date_joined',)
        }),
        (_('Orders'), {
            'fields': ('orders', ) 
        }),
    )

    search_fields = ('name', 'company_name', 'country', 'email', 'contact_person_name', 'address')
    ordering = ('company_name', 'country', 'name',)
    filter_horizontal = tuple()
    readonly_fields = ('last_login', 'date_joined',)

admin.site.register(SparmedUser, SparmedUserAdmin)
#admin.site.unregister(Group)

#from django.contrib.auth.models import Permission
#admin.site.register(Permission)