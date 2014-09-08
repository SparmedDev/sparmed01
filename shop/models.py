from django.db import models
from django import forms

from django.core.urlresolvers import reverse

from sorl.thumbnail import ImageField
import datetime
from validatedfile.fields import ValidatedFileField
from colorfield.fields import ColorField

class ProductImage(models.Model):
    image_title = models.CharField(max_length=200, verbose_name="Picture Title", blank=True)
    image = ImageField(upload_to="/media/products")
    product = models.ForeignKey('Product', related_name="images", verbose_name="Associated Product")

    def get_absolute_url(self):
      return u'%s' % self.image.url

    def __unicode__(self):
      return u'%s' % self.image_title

class GenericForm(forms.Form):
    q = forms.CharField(max_length=60, initial="Type a product name or ID here")
    
class Product(models.Model):
    product_id = models.CharField(max_length=255, verbose_name="Product ID", default="OOOO-0000")
    name = models.CharField(max_length=255, verbose_name="Product Name", default="Product 1")
    in_stock = models.IntegerField(verbose_name="Amount on Stock", default=0)
    description = models.CharField(max_length=255, verbose_name="Product description", blank=True)
    added = models.DateTimeField(default=datetime.datetime.now, verbose_name="Date and time added")
    slug = models.SlugField(unique=True, max_length=255, verbose_name="URL; Never modify this value!")
    subcategory = models.ForeignKey('Subcategory', related_name="products", verbose_name="Associated Subcategory")  
    order_index = models.PositiveIntegerField(blank=True, null=True, default=0)

    @property
    def category(self):
        return self.subcategory.category
    
    def get_absolute_url(self):
        return reverse('shop.views.details', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ['order_index']

    def __unicode__(self):
       return u'%s' % self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Subcategory Name", default="Subcategory 1")
    description = models.CharField(max_length=255, verbose_name="Subcategory description", blank=True)
    long_text = models.TextField(verbose_name="Subcategory Long Text (Please do not insert images!)", blank=True)
    added = models.DateTimeField(default=datetime.datetime.now, verbose_name="Date and time added")
    category = models.ForeignKey('Category', related_name="subcategories", verbose_name="Associated Category")
    color = ColorField(null=True, blank=True, verbose_name="Subcategory Color")
    order_index = models.PositiveIntegerField(blank=True, null=True, default=0)

    def get_absolute_url(self):
        return reverse('shop.views.products', args=[self.category.slug,])

    class Meta:
        ordering = ['order_index']
        verbose_name_plural = ('Subcategories')

    def __unicode__(self):
       return u'%s' % self.name

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Category Name", default="Category 1")
    short_name = models.CharField(max_length=20, verbose_name="Category Short Name (for navigation bar)", default="Cat1")
    description = models.CharField(max_length=255, verbose_name="Category description", blank=True)
    long_text = models.TextField(verbose_name="Category Long Text (Please do not insert images!)", blank=True)
    added = models.DateTimeField(default=datetime.datetime.now, verbose_name="Date and time added")
    slug = models.SlugField(unique=True, max_length=255, verbose_name="URL; Never modify this value!")
    
    document = ValidatedFileField(blank=True, null=True, verbose_name="PDF Document file (256 MB max)", upload_to='/documents/', content_types=['application/pdf'], max_upload_size=1024*1024*256)
    
    order_index = models.PositiveIntegerField(blank=True, null=True, default=0)

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