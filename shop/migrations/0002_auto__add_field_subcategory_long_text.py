# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Subcategory.long_text'
        db.add_column(u'shop_subcategory', 'long_text',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Subcategory.long_text'
        db.delete_column(u'shop_subcategory', 'long_text')


    models = {
        u'shop.category': {
            'Meta': {'ordering': "['-added']", 'object_name': 'Category'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Category 1'", 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'shop.product': {
            'Meta': {'ordering': "['-added']", 'object_name': 'Product'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Category']", 'related_name': "'products'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_stock': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Product 1'", 'max_length': '255'}),
            'product_id': ('django.db.models.fields.CharField', [], {'default': "'OOOO-0000'", 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Subcategory']", 'related_name': "'products'"})
        },
        u'shop.productimage': {
            'Meta': {'object_name': 'ProductImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'image_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Product']", 'related_name': "'images'"})
        },
        u'shop.subcategory': {
            'Meta': {'ordering': "['-added']", 'object_name': 'Subcategory'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop.Category']", 'related_name': "'subcategories'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_text': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Subcategory 1'", 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['shop']