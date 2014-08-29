from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django import forms
import datetime

from django.template.defaultfilters import slugify
from django_countries.fields import CountryField

class SparmedUserManager(BaseUserManager):
    def create_user(self, name, country, address, city, postal_code, contact_person_name, contact_telephone, email, password):
        if not name:
            raise ValueError('Users must have a company name')
        elif not country:
            raise ValueError('Users must have a company country')
        elif not address:
            raise ValueError('Users must have a company address')
        elif not city:
            raise ValueError('Users must have a company city')
        elif not postal_code:
            raise ValueError('Users must have a company postal code')
        elif not contact_person_name:
            raise ValueError('Users must have a valid contact person name')
        elif not contact_telephone:
            raise ValueError('Users must have a valid contact telephone number')
        elif not email:
            raise ValueError('Users must have an email address')
            
        user = self.model(
            name=name,
            country=country,
            address=address,
            city=city,
            postal_code=postal_code,
            contact_person_name=contact_person_name,
            contact_telephone=contact_telephone,
            email=self.normalize_email(email),
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
      
    def create_superuser(self, name, country, address, city, postal_code, contact_person_name, contact_telephone, email, password):                   
        user = self.create_user(
            name=name,
            country=country,
            address=address,
            city=city,
            postal_code=postal_code,
            contact_person_name=contact_person_name,
            contact_telephone=contact_telephone,
            email=self.normalize_email(email),
            password=password,
        )
      
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class SparmedUser(AbstractBaseUser):
    name = models.CharField(max_length=255, verbose_name="Sparmed Website Account Name", unique=True)
    company_name = models.CharField(max_length=255, verbose_name="Company Name")
    country = CountryField()
    address = models.CharField(max_length=255, verbose_name="Company Address")
    city = models.CharField(max_length=255, verbose_name="Company City")
    postal_code = models.IntegerField(verbose_name="Company Postal Code")
    contact_person_name = models.CharField(max_length=255, verbose_name="Company Contact Person Name")
    contact_telephone = models.IntegerField(max_length=20, unique=True)
    email = models.EmailField(verbose_name="Contact Email Address", max_length=255, unique=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = SparmedUserManager()
    
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['company_name', 'country', 'address', 'city', 'postal_code', 'contact_person_name', 'contact_telephone', 'email']
    
    def get_full_name(self):
        return self.company_name

    def get_short_name(self):
        return self.name

    def __unicode__(self):
        return self.name    
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
      
    @property
    def slug(self):
        return slugify(self.name)
      
    def get_absolute_url(self):
        return reverse('online_order.views.account_area', args=[self.slug])

class OrderForm(forms.Form):
    date = forms.DateTimeField(initial=datetime.datetime.now, label="Date and time ordered")
    
    arranged_freight = forms.BooleanField(label="SparMED Arranges Freight?", initial=True)
    freight_forwarder = forms.CharField(max_length=255, label="Freight Forwarder (if not through SparMed)", required=False)
    account_no = forms.CharField(max_length=255, label="Account Number (if not freight through SparMed)", required=False)
    
    EURO_PALLET = 'EP'
    HALF_PALLET = 'HP'
    BOX = 'BX'    
    PACKING_CHOICES = (
      (EURO_PALLET, 'Euro Pallet'),
      (HALF_PALLET, 'Half Pallet'),
      (BOX, 'Box'),
    )    
    packing_instructions = forms.CharField(max_length=2, widget=forms.Select(choices=PACKING_CHOICES))
    packing_remarks = forms.CharField(widget=forms.Textarea, label="Packaging Remarks/Comments", required=False)
    
    CARDBOARD_BOX = 'CB'
    WOODEN_FRAMES = 'WF'
    AIRCLEANER_CHOICES = (
      (CARDBOARD_BOX, 'Cardboard Box'),
      (WOODEN_FRAMES, 'Wooden Frames'),
    )    
    aircleaner_instructions = forms.CharField(max_length=2, widget=forms.Select(choices=AIRCLEANER_CHOICES))
    
    insurance_desired = forms.BooleanField(label="Insurance is Desired? (if freight is arranged by SparMed)", initial=False)
    
    documents = forms.CharField(widget=forms.Textarea, label="Please write down if you need any documents along with your shipment", required=False)
  
    shipping_and_invoice_same = forms.BooleanField(label="Shipping and invoice addresses are the same?", initial=True)
    invoice_company_name = forms.CharField(max_length=255, label="Invoice Company Name", required=False)
    invoice_company_address = forms.CharField(max_length=255, label="Invoice Company Address", required=False)
    invoice_company_country = forms.CharField(max_length=255, label="Invoice Company Country", required=False)
    invoice_company_postal_code = forms.IntegerField(label="Invoice Company Postal Code", required=False)
    
    other_remarks = forms.CharField(widget=forms.Textarea, label="Any other remarks or comments regarding this order?")
    
    
    
