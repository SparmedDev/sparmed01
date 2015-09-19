from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from sorl.thumbnail import ImageField
from django.utils import timezone
from validatedfile.fields import ValidatedFileField
from colorfield.fields import ColorField

from django.template.defaultfilters import slugify

from ckeditor.fields import RichTextField

class ProductImage(models.Model):
    image_title = models.CharField(max_length=200, verbose_name=_("Picture Title"), blank=True)
    image = ImageField(upload_to="media/products/")
    image_hires = ImageField(upload_to="media/products/", blank=True, null=True)
    product = models.ForeignKey('Product', related_name="images", verbose_name=_("Associated Product"))

    def get_absolute_url(self):
      return u'%s' % self.image.url

    def get_hires_url(self):
      if self.image_hires:
          return u'%s' % self.image_hires.url
      else:
          return self.get_absolute_url()

    def __unicode__(self):
      return u'%s' % self.image_title

class ShopImage(models.Model):
    image_title = models.CharField(max_length=255, verbose_name=_("Picture Title"), blank=True)
    image = ImageField(upload_to="media/products/")
    image_hires = ImageField(upload_to="media/products/", blank=True, null=True)

    subcategory = models.ForeignKey('Subcategory', related_name="images", verbose_name=_("Associated Subcategory"), blank=True, null=True)
    category = models.ForeignKey('Category', related_name="images", verbose_name=_("Associated Category"), blank=True, null=True)

    def get_absolute_url(self):
      return u'%s' % self.image.url

    def get_hires_url(self):
      if self.image_hires:
          return u'%s' % self.image_hires.url
      else:
          return self.get_absolute_url()

    def __unicode__(self):
      return u'%s' % self.image_title

class GenericForm(forms.Form):
    q = forms.CharField(max_length=60, initial=_("Type a product name or Order No. here"))

class Product(models.Model):
    product_id = models.CharField(max_length=255, verbose_name=_("Order No."), default="OOOO-0000")
    name = models.CharField(max_length=100, verbose_name=_("Product Short Name"))
    long_name = models.CharField(max_length=255, verbose_name=_("Product Long Name"), blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name=_("Product Description"), blank=True)
    long_text = RichTextField(verbose_name=_("Product Long Text"), blank=True, null=True)
    in_stock = models.IntegerField(verbose_name=_("Amount on Stock"), default=0)
    added = models.DateTimeField(default=timezone.now, verbose_name=_("Date and time added"))
    slug = models.SlugField(unique=True, max_length=255, verbose_name=_("URL; Never modify this value!"))
    subcategory = models.ForeignKey('Subcategory', related_name="products", verbose_name=_("Associated Subcategory"))
    order_index = models.PositiveIntegerField(blank=True, null=True, default=0)
    # Translators: (LxDxH) = Length x Depth x Height
    size = models.CharField(max_length=255, verbose_name=_("Size (LxDxH)"), blank=True, null=True)
    weight = models.CharField(max_length=255, verbose_name=_("Weight"), blank=True, null=True)
    hs_code = models.CharField(max_length=255, verbose_name=_("Tariff No. / HS Code"), blank=True, null=True)
    price = models.FloatField(verbose_name=_("Price"), blank=True, null=True)

    def save(self, *args, **kwargs):
        new_slug = slugify(self.product_id)
        if new_slug != self.slug:
            self.slug = new_slug

        super(Product, self).save(*args, **kwargs)

    @property
    def category(self):
        return self.subcategory.category

    def get_name(self):
        return self.long_name if self.long_name else self.name

    def get_absolute_url(self):
        return reverse('shop.views.details', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ['order_index', 'added']

    def __unicode__(self):
       return u'%s' % self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Subcategory Name"))
    description = models.CharField(max_length=255, verbose_name=_("Subcategory description"), blank=True)
    long_text = RichTextField(verbose_name=_("Subcategory Long Text (Please do not insert images!)"), blank=True)
    added = models.DateTimeField(default=timezone.now, verbose_name=_("Date and time added"))
    category = models.ForeignKey('Category', related_name="subcategories", verbose_name=_("Associated Category"))
    color = ColorField(verbose_name=_("Subcategory Color"), default='008393')
    order_index = models.PositiveIntegerField(blank=True, null=True, default=0)
    hs_code = models.CharField(max_length=255, verbose_name=_("Tariff No. / HS Code"), blank=True, null=True)

    @property
    def slug(self):
        return slugify(self.name)

    def get_absolute_url(self):
        return reverse('shop.views.products', args=[self.category.slug,])

    class Meta:
        ordering = ['order_index']
        verbose_name_plural = ('Subcategories')

    def __unicode__(self):
       return u'%s' % self.name

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Category Name"))
    short_name = models.CharField(max_length=40, verbose_name=_("Category Short Name (for navigation bar)"))
    description = models.CharField(max_length=255, verbose_name=_("Category description"), blank=True)
    long_text = RichTextField(verbose_name=_("Category Long Text (Please do not insert images!)"), blank=True)
    added = models.DateTimeField(default=timezone.now, verbose_name=_("Date and time added"))
    slug = models.SlugField(unique=True, max_length=255, verbose_name=_("URL; Never modify this value!"))
    order_index = models.PositiveIntegerField(blank=True, null=True, default=0)
    hs_code = models.CharField(max_length=255, verbose_name=_("Tariff No. / HS Code"), blank=True, null=True)

    document = ValidatedFileField(blank=True, null=True, verbose_name=_("PDF Document file (56 MB max)"), upload_to='documents/', content_types=['application/pdf'], max_upload_size=1024*1024*56)

    def save(self, *args, **kwargs):
        new_slug = slugify(self.short_name)
        if new_slug != self.slug:
            self.slug = new_slug

        super(Category, self).save(*args, **kwargs)

    @property
    def products(self):
        id_list = []

        for subcat in self.subcategories.all():
            id_list += [product.pk for product in subcat.products.all()]

        return Product.objects.filter(pk__in=id_list)

    def get_absolute_url(self):
        return reverse('shop.views.products', args=[self.slug,])

    class Meta:
        ordering = ['order_index']
        verbose_name_plural = ('Categories')

    def __unicode__(self):
       return u'%s' % self.name