# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductImage'
        db.create_table(u'shop_productimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_title', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['shop.Product'])),
        ))
        db.send_create_signal(u'shop', ['ProductImage'])

        # Adding model 'Product'
        db.create_table(u'shop_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_id', self.gf('django.db.models.fields.CharField')(default='OOOO-0000', max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Product 1', max_length=255)),
            ('in_stock', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, unique=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='products', to=orm['shop.Category'])),
            ('subcategory', self.gf('django.db.models.fields.related.ForeignKey')(related_name='products', to=orm['shop.Subcategory'])),
        ))
        db.send_create_signal(u'shop', ['Product'])

        # Adding model 'Subcategory'
        db.create_table(u'shop_subcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Subcategory 1', max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, unique=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='subcategories', to=orm['shop.Category'])),
        ))
        db.send_create_signal(u'shop', ['Subcategory'])

        # Adding model 'Category'
        db.create_table(u'shop_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Category 1', max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, unique=True)),
        ))
        db.send_create_signal(u'shop', ['Category'])


    def backwards(self, orm):
        # Deleting model 'ProductImage'
        db.delete_table(u'shop_productimage')

        # Deleting model 'Product'
        db.delete_table(u'shop_product')

        # Deleting model 'Subcategory'
        db.delete_table(u'shop_subcategory')

        # Deleting model 'Category'
        db.delete_table(u'shop_category')


    models = {
        u'shop.category': {
            'Meta': {'ordering': "['-added']", 'object_name': 'Category'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Category 1'", 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True'})
        },
        u'shop.product': {
            'Meta': {'ordering': "['-added']", 'object_name': 'Product'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': u"orm['shop.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_stock': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Product 1'", 'max_length': '255'}),
            'product_id': ('django.db.models.fields.CharField', [], {'default': "'OOOO-0000'", 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': u"orm['shop.Subcategory']"})
        },
        u'shop.productimage': {
            'Meta': {'object_name': 'ProductImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'image_title': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['shop.Product']"})
        },
        u'shop.subcategory': {
            'Meta': {'ordering': "['-added']", 'object_name': 'Subcategory'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subcategories'", 'to': u"orm['shop.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Subcategory 1'", 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True'})
        }
    }

    complete_apps = ['shop']