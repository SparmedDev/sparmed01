from django import forms
from django.utils.translation import ugettext as _
from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    sender_name = forms.CharField(max_length=200, label=_("Sender Full Name"))
    sender = forms.EmailField(label=_("Sender Email Address"))
    cc_myself = forms.BooleanField(required=False, label=_("Send copy to my own email"))
    subject = forms.CharField(max_length=100, label=_("Message Subject"))
    message = forms.CharField(widget=forms.Textarea, label=_("Message Body Text"))
    captcha = ReCaptchaField(attrs={'theme' : 'clean'})