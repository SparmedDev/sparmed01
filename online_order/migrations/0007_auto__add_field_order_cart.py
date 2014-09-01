# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.cart'
        db.add_column(u'online_order_order', 'cart',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cart.Cart'], null=True, related_name='cart', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Order.cart'
        db.delete_column(u'online_order_order', 'cart_id')


    models = {
        u'cart.cart': {
            'Meta': {'ordering': "('-creation_date',)", 'object_name': 'Cart'},
            'checked_out': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'online_order.order': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Order'},
            'account_no': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'}),
            'aircleaner_instructions': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '2'}),
            'arranged_freight': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cart.Cart']", 'null': 'True', 'related_name': "'cart'", 'blank': 'True'}),
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
            'packing_instructions': ('django.db.models.fields.CharField', [], {'default': "'EP'", 'max_length': '2'}),
            'packing_remarks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'shipping_and_invoice_same': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
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
            'orders': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['online_order.Order']", 'null': 'True', 'related_name': "'orders'", 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'postal_code': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['online_order']