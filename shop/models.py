from django.db import models
from django import forms

from django.core.urlresolvers import reverse

from sorl.thumbnail import ImageField
from django.utils import timezone
from validatedfile.fields import ValidatedFileField
from colorfield.fields import ColorField

from django.template.defaultfilters import slugify

from ckeditor.fields import RichTextField

class ProductImage(models.Model):
    image_title = models.CharField(max_length=200, verbose_name="Picture Title", blank=True)
    image = ImageField(upload_to="/media/products")
    product = models.ForeignKey('Product', related_name="images", verbose_name="Associated Product")

    def get_absolute_url(self):
      return u'%s' % self.image.url

    def __unicode__(self):
      return u'%s' % self.image_title
    
class ShopImage(models.Model):
    image_title = models.CharField(max_length=255, verbose_name="Picture Title", blank=True)
    image = ImageField(upload_to="/media/products")    
    
    subcategory = models.ForeignKey('Subcategory', related_name="images", verbose_name="Associated Subcategory", blank=True, null=True)
    category = models.ForeignKey('Category', related_name="images", verbose_name="Associated Category", blank=True, null=True)

    def get_absolute_url(self):
      return u'%s' % self.image.url

    def __unicode__(self):
      return u'%s' % self.image_title    

class GenericForm(forms.Form):
    q = forms.CharField(max_length=60, initial="Type a product name or ID here")
    
class Product(models.Model):
    product_id = models.CharField(max_length=255, verbose_name="Product ID", default="OOOO-0000")
    name = models.CharField(max_length=100, verbose_name="Product Short Name", default="Product 1")
    long_name = models.CharField(max_length=255, verbose_name="Product Long Name", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="Product Description", blank=True)
    long_text = RichTextField(verbose_name="Product Long Text", blank=True, null=True)
    in_stock = models.IntegerField(verbose_name="Amount on Stock", default=0)    
    added = models.DateTimeField(default=timezone.now, verbose_name="Date and time added")
    slug = models.SlugField(unique=True, max_length=255, verbose_name="URL; Never modify this value!")
    subcategory = models.ForeignKey('Subcategory', related_name="products", verbose_name="Associated Subcategory")  
    order_index = models.PositiveIntegerField(blank=True, null=True, default=0)
    size = models.CharField(max_length=255, verbose_name="Size (LxDxH)", blank=True, null=True)
    weight = models.CharField(max_length=255, verbose_name="Weight", blank=True, null=True)
    hs_code = models.CharField(max_length=255, verbose_name="Tariff No. / HS Code", blank=True, null=True)
    price = models.FloatField(verbose_name="Price", blank=True, null=True)

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
    name = models.CharField(max_length=255, verbose_name="Subcategory Name", default="Subcategory 1")
    description = models.CharField(max_length=255, verbose_name="Subcategory description", blank=True)
    long_text = RichTextField(verbose_name="Subcategory Long Text (Please do not insert images!)", blank=True)
    added = models.DateTimeField(default=timezone.now, verbose_name="Date and time added")
    category = models.ForeignKey('Category', related_name="subcategories", verbose_name="Associated Category")
    color = ColorField(verbose_name="Subcategory Color", default='008393')
    order_index = models.PositiveIntegerField(blank=True, null=True, default=0)
    hs_code = models.CharField(max_length=255, verbose_name="Tariff No. / HS Code", blank=True, null=True)

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
    name = models.CharField(max_length=255, verbose_name="Category Name", default="Category 1")
    short_name = models.CharField(max_length=40, verbose_name="Category Short Name (for navigation bar)", default="Cat1")
    description = models.CharField(max_length=255, verbose_name="Category description", blank=True)
    long_text = RichTextField(verbose_name="Category Long Text (Please do not insert images!)", blank=True)
    added = models.DateTimeField(default=timezone.now, verbose_name="Date and time added")
    slug = models.SlugField(unique=True, max_length=255, verbose_name="URL; Never modify this value!")
    order_index = models.PositiveIntegerField(blank=True, null=True, default=0)
    hs_code = models.CharField(max_length=255, verbose_name="Tariff No. / HS Code", blank=True, null=True)
    
    document = ValidatedFileField(blank=True, null=True, verbose_name="PDF Document file (56 MB max)", upload_to='/documents/', content_types=['application/pdf'], max_upload_size=1024*1024*56)

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