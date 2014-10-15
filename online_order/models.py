from django import forms
from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import datetime

from django.template.defaultfilters import slugify
from django_countries.fields import CountryField


class SparmedUserManager(BaseUserManager):
    def create_user(self, name, company_name, country, address, city, postal_code, contact_person_name, contact_telephone, email, password):
        if not name:
            raise ValueError('Users must have a Sparmed website account name')
        if not company_name:
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
            company_name=company_name,
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
      
    def create_superuser(self, name, company_name, country, address, city, postal_code, contact_person_name, contact_telephone, email, password):                   
        user = self.create_user(
            name=name,
            company_name=company_name,
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
    postal_code = models.CharField(max_length=255, verbose_name="Company Postal Code", blank=True, null=True)
    contact_person_name = models.CharField(max_length=255, verbose_name="Company Contact Person Name")
    contact_telephone = models.IntegerField(max_length=20, unique=True, verbose_name="Contact Telephone Number")
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
      
    def add_to_order_history(self, order, items_list):
        if order and items_list:
            o_new = self.orders.create(
                arranged_freight=order.arranged_freight,
                freight_forwarder=order.freight_forwarder,
                account_no=order.account_no,
              
                arranged_packing=order.arranged_packing,
                packing_instructions=order.packing_instructions,
                packing_remarks=order.packing_remarks,
                
                aircleaner_instructions=order.aircleaner_instructions,
                insurance_desired=order.insurance_desired,
                documents=order.documents,
              
                shipping_and_invoice_same=order.shipping_and_invoice_same,
                invoice_company_name=order.invoice_company_name,
                invoice_company_address=order.invoice_company_address,
                invoice_company_postal_code=order.invoice_company_postal_code,
                invoice_company_country=order.invoice_company_country,
              
                other_remarks=order.other_remarks,            
                
                user=self,
            )
            
            if o_new:     
                for item in items_list:
                    o_new.items.create(
                        quantity=item.quantity,
                        object_id=item.object_id,

                        product_id=item.product.product_id,
                        name=item.product.name,
                        description=item.product.description,
                        slug=item.product.slug,
                      
                        category_slug=item.product.category.slug,

                        order_history=o_new,  
                     )
              
                o_new.save()
                self.save()
                return o_new
            else:
                raise ValueError('Order history item instantiation failed, o new is null')
        else:
            raise ValueError('Cannot add null order or empty items list to order history')

      
class Order(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now, verbose_name="Date and time of order")
    
    arranged_freight = models.BooleanField(verbose_name="SparMED Arranges Freight?", default=True)
    freight_forwarder = models.CharField(max_length=255, verbose_name="Freight Forwarder", blank=True, null=True)
    account_no = models.CharField(max_length=255, verbose_name="Account Number", blank=True, null=True)
    
    EURO_PALLET = 'EP'
    HALF_PALLET = 'HP'
    BOX = 'BX'    
    PACKING_CHOICES = (
      (EURO_PALLET, 'Euro Pallet'),
      (HALF_PALLET, 'Half Pallet'),
      (BOX, 'Box'),
    )  
    
    arranged_packing = models.BooleanField(verbose_name="SparMED Arranges Packaging?", default=True)
    packing_instructions = models.CharField(verbose_name="Packaging Instructions", max_length=2, choices=PACKING_CHOICES, default=EURO_PALLET, help_text="Please note if nothing is filled out SparMED will choose the best and safest way of packing your order.", blank=True)
    packing_remarks = models.TextField(verbose_name="Packaging Remarks/Comments", blank=True, null=True)
    
    CARDBOARD_BOX = 'CB'
    WOODEN_FRAMES = 'WF'
    AIRCLEANER_CHOICES = (
      (CARDBOARD_BOX, 'Cardboard Box'),
      (WOODEN_FRAMES, 'Wooden Frames'),
    )    
    aircleaner_instructions = models.CharField(verbose_name="Aircleaner Instructions (If applicable)", max_length=2, choices=AIRCLEANER_CHOICES, blank=True, null=True)
    
    insurance_desired = models.BooleanField(verbose_name="Is insurance needed?", default=False, blank=True)
    
    documents = models.TextField(verbose_name="Please write down if you need any specific documents along with your shipment", blank=True, null=True)
    
    shipping_and_invoice_same = models.BooleanField(verbose_name="Different delivery address?", default=True, blank=True)
    invoice_company_name = models.CharField(max_length=255, verbose_name="Company Name", blank=True, null=True)
    invoice_company_address = models.CharField(max_length=255, verbose_name="Delivery Address", blank=True, null=True)
    invoice_company_postal_code = models.IntegerField(verbose_name="Delivery Postal Code", blank=True, null=True)    
    invoice_company_country = CountryField(verbose_name="Delivery Country", blank=True, null=True)
    
    other_remarks = models.TextField(verbose_name="Any other remarks or comments regarding this order?", blank=True, null=True)
    
    class Meta:
        ordering = ['-date']        
      
class OrderForm(ModelForm):  
    arranged_freight = forms.BooleanField(label="SparMED Arranges Freight?", initial=True, required=False)
    arranged_packing = forms.BooleanField(label="SparMED Arranges Packaging?", initial=True, required=False)
    insurance_desired = forms.BooleanField(label="Is insurance needed?", initial=False, required=False)
    shipping_and_invoice_same = forms.BooleanField(label="Different delivery address?", initial=True, required=False)
  
    class Meta:
        model = Order
        exclude = ['date']
        

class OrderHistoryItem(Order):
    user = models.ForeignKey('SparmedUser', related_name='orders', null=True, blank=True)

    
class OrderProduct(models.Model):
    quantity = models.PositiveIntegerField(verbose_name='quantity')
    object_id = models.PositiveIntegerField()
    
    product_id = models.CharField(max_length=255, verbose_name="Product ID", default="OOOO-0000")
    name = models.CharField(max_length=255, verbose_name="Product Name", default="Product 1")    
    description = models.CharField(max_length=255, verbose_name="Product Long Name", blank=True, null=True)
    category_slug = models.SlugField(max_length=255, verbose_name="URL; Never modify this value!")
    slug = models.SlugField(max_length=255, verbose_name="URL; Never modify this value!")
    
    order_history = models.ForeignKey('OrderHistoryItem', related_name='items')
    
    def get_absolute_url(self):
        return reverse('shop.views.details', args=[self.category_slug, self.slug,])   
      
    def __unicode__(self):
       return u'%s - %s' % (self.product_id, self.name)