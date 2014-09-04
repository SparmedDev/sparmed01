# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'OrderProduct', fields ['slug']
        db.delete_unique(u'online_order_orderproduct', ['slug'])


    def backwards(self, orm):
        # Adding unique constraint on 'OrderProduct', fields ['slug']
        db.create_unique(u'online_order_orderproduct', ['slug'])


    models = {
        u'online_order.order': {
            'Meta': {'object_name': 'Order', 'ordering': "['-date']"},
            'account_no': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'}),
            'aircleaner_instructions': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '2'}),
            'arranged_freight': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'documents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'freight_forwarder': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance_desired': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'invoice_company_address': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'}),
            'invoice_company_country': ('django_countries.fields.CountryField', [], {'null': 'True', 'blank': 'True', 'max_length': '2'}),
            'invoice_company_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'}),
            'invoice_company_postal_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'other_remarks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'packing_instructions': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'EP'", 'max_length': '2'}),
            'packing_remarks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'shipping_and_invoice_same': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'online_order.orderhistoryitem': {
            'Meta': {'object_name': 'OrderHistoryItem', 'ordering': "['-date']", '_ormbases': [u'online_order.Order']},
            u'order_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': u"orm['online_order.Order']", 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders'", 'null': 'True', 'blank': 'True', 'to': u"orm['online_order.SparmedUser']"})
        },
        u'online_order.orderproduct': {
            'Meta': {'object_name': 'OrderProduct'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Product 1'", 'max_length': '255'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order_history': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['online_order.OrderHistoryItem']"}),
            'product_id': ('django.db.models.fields.CharField', [], {'default': "'OOOO-0000'", 'max_length': '255'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        },
        u'online_order.sparmeduser': {
            'Meta': {'object_name': 'SparmedUser'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_person_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_telephone': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '20'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'postal_code': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['online_order']