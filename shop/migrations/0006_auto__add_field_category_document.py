# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.document'
        db.add_column(u'shop_category', 'document',
                      self.gf('validatedfile.fields.ValidatedFileField')(null=True, content_types=['application/pdf'], blank=True, max_upload_size=268435456, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.document'
        db.delete_column(u'shop_category', 'document')


    models = {
        u'shop.category': {
            'Meta': {'ordering': "['-added']", 'object_name': 'Category'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'document': ('validatedfile.fields.ValidatedFileField', [], {'null': 'True', 'content_types': "['application/pdf']", 'blank': 'True', 'max_upload_size': '268435456', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'Category 1'"}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'Cat1'"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'shop.product': {
            'Meta': {'ordering': "['-added']", 'object_name': 'Product'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': u"orm['shop.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_stock': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'Product 1'"}),
            'product_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'OOOO-0000'"}),
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
            'Meta': {'ordering': "['-added']", 'object_name': 'Subcategory'},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subcategories'", 'to': u"orm['shop.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'Subcategory 1'"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['shop']