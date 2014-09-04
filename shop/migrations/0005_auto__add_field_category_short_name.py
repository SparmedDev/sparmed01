# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.short_name'
        db.add_column(u'shop_category', 'short_name',
                      self.gf('django.db.models.fields.CharField')(default='Cat1', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.short_name'
        db.delete_column(u'shop_category', 'short_name')


    models = {
        u'shop.category': {
            'Meta': {'object_name': 'Category', 'ordering': "['-added']"},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Category 1'", 'max_length': '255'}),
            'short_name': ('django.db.models.fields.CharField', [], {'default': "'Cat1'", 'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'shop.product': {
            'Meta': {'object_name': 'Product', 'ordering': "['-added']"},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': u"orm['shop.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_stock': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Product 1'", 'max_length': '255'}),
            'product_id': ('django.db.models.fields.CharField', [], {'default': "'OOOO-0000'", 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
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
            'Meta': {'object_name': 'Subcategory', 'ordering': "['-added']"},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subcategories'", 'to': u"orm['shop.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Subcategory 1'", 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['shop']