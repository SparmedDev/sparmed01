from django import forms
from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils.http import urlquote
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django_countries.fields import CountryField
from django.core.mail import send_mail

class SparmedUserManager(BaseUserManager):

    def _create_user(self, name, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        elif not name:
            raise ValueError('An account name must be given')

        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(username=name, name=name, email=email, is_active=True,
                          is_superuser=is_superuser, is_admin=is_admin, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name, email, password=None, **extra_fields):
        return self._create_user(name, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, name, email, password, **extra_fields):
        return self._create_user(name, email, password, True, True,
                                 **extra_fields)

class SparmedUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, verbose_name=_("Sparmed Client No."), unique=True)
    company_name = models.CharField(max_length=255, verbose_name=("Company Name"), blank=True)
    country = CountryField(blank=True)
    address = models.CharField(max_length=255, verbose_name=("Company Address"), blank=True)
    city = models.CharField(max_length=255, verbose_name=_("Company City"), blank=True)
    postal_code = models.CharField(max_length=255, verbose_name=_("Company Postal Code"), blank=True, null=True)
    contact_person_name = models.CharField(max_length=255, verbose_name=_("Company Contact Person Name"), blank=True)
    contact_telephone = models.CharField(max_length=50, verbose_name=_("Contact Telephone Number"), blank=True)
    email = models.EmailField(verbose_name=_("Contact Email Address"), max_length=255, unique=True)
    date_joined = models.DateTimeField(_("Date joined"), default=timezone.now, blank=True, null=True)

    is_active = models.BooleanField(_('Active'), default=True,
        help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    is_admin = models.BooleanField(default=False,
        help_text=_('Designates whether the user can log into this admin site.'))
    is_staff = models.BooleanField(default=True,
        help_text=_('Designates whether the user is regarded as staff'))

    objects = SparmedUserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['company_name', 'country', 'address', 'city', 'postal_code', 'contact_person_name', 'contact_telephone', 'email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __unicode__(self):
        return self.name

    def get_full_name(self):
        return self.company_name

    def get_short_name(self):
        return self.name

    @property
    def slug(self):
        return slugify(self.name)

    def get_absolute_url(self):
        return reverse('online_order.views.account_area', args=[self.slug])

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def add_to_order_history(self, order, items_list, **kwargs):
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
            **kwargs
        )

        for item in items_list:
          o_new.items.create(
              quantity=item.quantity,
              object_id=item.object_id,

              product_id=item.product.product_id,
              name=item.product.name,
              long_name=item.product.long_name,
              description=item.product.description,
              slug=item.product.slug,

              category_slug=item.product.category.slug,

              order_history=o_new,
          )

        o_new.save()
        self.save()
        return o_new

class Order(models.Model):
    date = models.DateTimeField(default=timezone.now, verbose_name=_("Date and time of order"))

    arranged_freight = models.BooleanField(verbose_name=_("SparMED Arranges Freight?"), default=True)
    freight_forwarder = models.CharField(max_length=255, verbose_name=_("Freight Forwarder"), blank=True, null=True)
    account_no = models.CharField(max_length=255, verbose_name=_("Account Number"), blank=True, null=True)

    # Translators: Euro Pallet abbreviation 'EP'
    EURO_PALLET = _('EP')
    # Translators: Half Pallet abbreviation 'HP'
    HALF_PALLET = _('HP')
    # Translators: Box abbreviation 'BX'
    BOX = _('BX')
    PACKING_CHOICES = (
      (EURO_PALLET, _('Euro Pallet')),
      (HALF_PALLET, _('Half Pallet')),
      (BOX, _('Box')),
    )

    arranged_packing = models.BooleanField(verbose_name=_("SparMED Arranges Packaging?"), default=True)
    packing_instructions = models.CharField(verbose_name=_("Packaging Instructions"), max_length=2, choices=PACKING_CHOICES, default=EURO_PALLET, help_text=_("Please note if nothing is filled out SparMED will choose the best and safest way of packing your order."), blank=True)
    packing_remarks = models.TextField(verbose_name=_("Packaging Remarks/Comments"), blank=True, null=True)

    # Translators: Carboard Box abbreviation 'CB'
    CARDBOARD_BOX = _('CB')
    # Translators: Wooden Frames abbreviation 'WF'
    WOODEN_FRAMES = _('WF')
    AIRCLEANER_CHOICES = (
      (CARDBOARD_BOX, _('Cardboard Box')),
      (WOODEN_FRAMES, _('Wooden Frames')),
    )
    aircleaner_instructions = models.CharField(verbose_name=_("Aircleaner Instructions (If applicable)"), max_length=2, choices=AIRCLEANER_CHOICES, blank=True, null=True)

    insurance_desired = models.BooleanField(verbose_name=_("Is insurance needed?"), default=False, blank=True)

    documents = models.TextField(verbose_name=_("Please write down if you need any specific documents along with your shipment"), blank=True, null=True)

    shipping_and_invoice_same = models.BooleanField(verbose_name=_("Different delivery address?"), default=True, blank=True)
    invoice_company_name = models.CharField(max_length=255, verbose_name=_("Company Name"), blank=True, null=True)
    invoice_company_address = models.CharField(max_length=255, verbose_name=_("Delivery Address"), blank=True, null=True)
    invoice_company_postal_code = models.IntegerField(verbose_name=_("Delivery Postal Code"), blank=True, null=True)
    invoice_company_country = CountryField(verbose_name=_("Delivery Country"), blank=True, null=True)

    other_remarks = models.TextField(verbose_name=_("Any other remarks or comments regarding this order?"), blank=True, null=True)

    class Meta:
        ordering = ['-date']

class OrderForm(ModelForm):
    arranged_freight = forms.BooleanField(label=_("SparMED Arranges Freight?"), initial=True, required=False)
    arranged_packing = forms.BooleanField(label=_("SparMED Arranges Packaging?"), initial=True, required=False)
    insurance_desired = forms.BooleanField(label=_("Is insurance needed?"), initial=False, required=False)
    shipping_and_invoice_same = forms.BooleanField(label=_("Different delivery address?"), initial=True, required=False)

    class Meta:
        model = Order
        exclude = ['date']


class OrderHistoryItem(Order):
    user = models.ForeignKey('SparmedUser', related_name='orders', null=True, blank=True)


class OrderProduct(models.Model):
    quantity = models.PositiveIntegerField(verbose_name='quantity')
    object_id = models.PositiveIntegerField()

    product_id = models.CharField(max_length=255, verbose_name=_("Order No."), default="OOOO-0000")
    name = models.CharField(max_length=255, verbose_name=_("Product Name"), default="Product 1")
    long_name = models.CharField(max_length=255, verbose_name=_("Product Long Name"), blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name=_("Product Description"), blank=True, null=True)
    category_slug = models.SlugField(max_length=255, verbose_name=_("URL; Never modify this value!"))
    slug = models.SlugField(max_length=255, verbose_name=_("URL; Never modify this value!"))

    order_history = models.ForeignKey('OrderHistoryItem', related_name='items')

    def get_name(self):
        return self.long_name if self.long_name else self.name

    def get_absolute_url(self):
        return reverse('shop.views.details', args=[self.category_slug, self.slug,])

    def __unicode__(self):
       return u'%s - %s' % (self.product_id, self.name)


class InventoryAddToCartForm(forms.Form):
    product_id = forms.CharField()
    quantity = forms.IntegerField(min_value=1, initial=1)