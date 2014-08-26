from django.db import models
from django.core.urlresolvers import reverse

from sorl.thumbnail import ImageField
import datetime

from shop import views

class ProductImage(models.Model):
    image_title = models.CharField(max_length=200, verbose_name="Picture Title", blank=True)
    image = ImageField(upload_to="/media/products")
    product = models.ForeignKey('Product', related_name="images", verbose_name="Associated Product")

    def get_absolute_url(self):
      return u'%s' % self.image.url

    def __unicode__(self):
      return u'%s' % self.image_title

class Product(models.Model):
    product_id = models.CharField(max_length=255, verbose_name="Product #", default="OOOO-0000")
    name = models.CharField(max_length=255, verbose_name="Product Name", default="Product 1")
    in_stock = models.IntegerField(verbose_name="Amount on Stock", default=0)
    description = models.CharField(max_length=255, verbose_name="Product description", blank=True)
    added = models.DateTimeField(default=datetime.datetime.now, verbose_name="Date and time added")
    slug = models.SlugField(unique=True, max_length=255, verbose_name="URL; Never modify this value!")
    category = models.ForeignKey('Category', related_name="products", verbose_name="Associated Category")
    subcategory = models.ForeignKey('Subcategory', related_name="products", verbose_name="Associated Subcategory")

    def get_absolute_url(self):
        return reverse(views.details, args=[self.category.slug, self.slug])

    class Meta:
        ordering = ['-added']

    def __unicode__(self):
       return u'%s' % self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Subcategory Name", default="Subcategory 1")
    description = models.CharField(max_length=255, verbose_name="Subcategory description", blank=True)
    added = models.DateTimeField(default=datetime.datetime.now, verbose_name="Date and time added")
    slug = models.SlugField(unique=True, max_length=255, verbose_name="URL; Never modify this value!")
    category = models.ForeignKey('Category', related_name="subcategories", verbose_name="Associated Category")

    def get_absolute_url(self):
        return reverse(views.products, args=[self.category.slug,])

    class Meta:
        ordering = ['-added']

    def __unicode__(self):
       return u'%s' % self.name

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Category Name", default="Category 1")
    description = models.CharField(max_length=255, verbose_name="Category description", blank=True)
    added = models.DateTimeField(default=datetime.datetime.now, verbose_name="Date and time added")
    slug = models.SlugField(unique=True, max_length=255, verbose_name="URL; Never modify this value!")

    def get_absolute_url(self):
        return reverse(views.products, args=[self.slug,])

    class Meta:
        ordering = ['-added']

    def __unicode__(self):
       return u'%s' % self.name