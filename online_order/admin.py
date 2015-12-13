from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, PasswordResetForm, UserCreationForm, UserChangeForm
from django.utils.translation import ugettext, ugettext_lazy as _

from online_order.models import SparmedUser
#from authtools.forms import UserCreationForm, UserChangeForm
from django.utils.crypto import get_random_string


class SparmedUserChangeForm(UserChangeForm):
    class Meta:
      model = SparmedUser
      fields = '__all__'
      #exclude = ('is_staff',)
#    class Meta:
#        model = SparmedUser
#        fields = '__all__'

#    def __init__(self, *args, **kwargs):
#        super(SparmedUserChangeForm, self).__init__(*args, **kwargs)
        #self.fields['email'].required = True
        #self.fields['name'].required = True

#class UserCreationForm(UserCreationForm):
#    """
#    A UserCreationForm with optional password inputs.
#    """
#
#    def __init__(self, *args, **kwargs):
#        super(UserCreationForm, self).__init__(*args, **kwargs)
#        self.fields['password1'].required = False
#        self.fields['password2'].required = False
        # If one field gets autocompleted but not the other, our 'neither
        # password or both password' validation will be triggered.
#        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
#        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

#    def clean_password2(self):
#        password1 = self.cleaned_data.get("password1")
#        password2 = super(UserCreationForm, self).clean_password2()
#        if bool(password1) ^ bool(password2):
#            raise forms.ValidationError("Fill out both fields")
#        return password2

class SparmedUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = SparmedUserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name', 'company_name', 'email', 'contact_person_name', 'is_admin', 'country',)
    list_filter = ('is_admin', 'country',)

    exclude = ('first_name', 'last_name',)

    fieldsets = (
        (None, {
            'description': (
                _("Enter the new user's username and email address.")
            ),
            'fields': ('name', 'email',),
        }),
        (_('Password'), {
            #'description': _("You may set the user's password here."),
            'fields': ('password',),
            'classes': ('collapse', 'collapse-closed'),
        }),
        (_('Personal info'), {'fields': ('company_name', 'country', 'address', 'city', 'postal_code', 'contact_person_name', 'contact_telephone',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_admin', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'description': (
                _("Enter the new user's username and email address.")
            ),
            'fields': ('name', 'email',),
        }),
        (_('Password'), {
            'description': _("You may set the user's password here."),
            'fields': ('password1', 'password2'),
            'classes': ('collapse', 'collapse-closed'),
        }),
        (_('Personal info'), {'fields': ('company_name', 'country', 'address', 'city', 'postal_code', 'contact_person_name', 'contact_telephone',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_admin', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    search_fields = ('name', 'company_name', 'country', 'email', 'contact_person_name', 'address')
    ordering = ('company_name', 'country', 'name',)
    filter_horizontal = tuple()
    readonly_fields = ('last_login', 'date_joined',)

    #def save_model(self, request, obj, form, change):
      #name = form.cleaned_data.get('name')
      #username = form.cleaned_data.get('username')
      #if username:
      #    self.name = username
      #elif name:
          #self.username = name

      #super(UserAdmin, self).save_model(request, obj, form, change)
      #if not change and (not form.cleaned_data['password1'] or not obj.has_usable_password()):
        # Django's PasswordResetForm won't let us reset an unusable
        # password. We set it above super() so we don't have to save twice.
      #  obj.set_password(get_random_string())
      #  reset_password = True
      #else:
      #  reset_password = False

      #super(UserAdmin, self).save_model(request, obj, form, change)

      #if reset_password:
      #  reset_form = PasswordResetForm({'email': obj.email})
      #  assert reset_form.is_valid()
      #  reset_form.save(
      #    request=request,
      #    use_https=request.is_secure(),
          #subject_template_name='registration/account_creation_subject.txt',
          #email_template_name='registration/account_creation_email.html',
      #  )

admin.site.register(SparmedUser, SparmedUserAdmin)
#admin.site.unregister(Group)

#from django.contrib.auth.models import Permission
#admin.site.register(Permission)