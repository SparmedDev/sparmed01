from django.db import models
from django import forms
from captcha.fields import ReCaptchaField

# Create your models here.

class ContactForm(forms.Form):
    sender_name = forms.CharField(max_length=200, label="Sender Full Name")
    sender = forms.EmailField(label="Sender Email Address")
    cc_myself = forms.BooleanField(required=False, label="Send copy to my own email")
    subject = forms.CharField(max_length=100, label="Message Subject")
    message = forms.CharField(widget=forms.Textarea, label="Message Body Text")
    captcha = ReCaptchaField()
