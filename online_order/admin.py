from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from online_order.models import SparmedUser
# Register your models here.

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)  
    
    class Meta:
        model = SparmedUser
        fields = ('name', 'company_name', 'email', 'contact_person_name')
                  
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user                  
                  
                  
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = SparmedUser
        fields = ('name', 'company_name', 'email', 'password', 'contact_person_name', 'is_active', 'is_admin',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]                  
      
class SparmedUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = SparmedUser
        fields = ('name', 'company_name', 'country', 'address', 'city', 'postal_code', 'email', 'contact_person_name', 'contact_telephone', 'password',)

    def clean_password(self):
        return self.initial["password"]   
 

class SparmedUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name', 'company_name', 'email', 'contact_person_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}),
        ('Personal info', {'fields': ('company_name', 'country', 'address', 'city', 'postal_code', 'contact_person_name', 'contact_telephone',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'company_name', 'country', 'address', 'city', 'postal_code', 'contact_person_name', 'contact_telephone', 'password1', 'password2')}
        ),
    )
    search_fields = ('name', 'company_name', 'country', 'email', 'contact_person_name', 'address')
    ordering = ('company_name', 'country', 'name',)
    filter_horizontal = () 

admin.site.register(SparmedUser, SparmedUserAdmin)
admin.site.unregister(Group)