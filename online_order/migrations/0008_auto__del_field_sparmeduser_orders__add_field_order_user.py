# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SparmedUser.orders'
        db.delete_column(u'online_order_sparmeduser', 'orders_id')

        # Adding field 'Order.user'
        db.add_column(u'online_order_order', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='orders', blank=True, to=orm['online_order.SparmedUser'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'SparmedUser.orders'
        db.add_column(u'online_order_sparmeduser', 'orders',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='orders', blank=True, to=orm['online_order.Order'], null=True),
                      keep_default=False)

        # Deleting field 'Order.user'
        db.delete_column(u'online_order_order', 'user_id')


    models = {
        u'cart.cart': {
            'Meta': {'ordering': "('-creation_date',)", 'object_name': 'Cart'},
            'checked_out': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'online_order.order': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Order'},
            'account_no': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'aircleaner_instructions': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'arranged_freight': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'order'", 'blank': 'True', 'to': u"orm['cart.Cart']", 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'documents': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'freight_forwarder': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance_desired': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'invoice_company_address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'invoice_company_country': ('django_countries.fields.CountryField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'invoice_company_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'invoice_company_postal_code': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'other_remarks': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'packing_instructions': ('django.db.models.fields.CharField', [], {'default': "'EP'", 'max_length': '2'}),
            'packing_remarks': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'shipping_and_invoice_same': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders'", 'blank': 'True', 'to': u"orm['online_order.SparmedUser']", 'null': 'True'})
        },
        u'online_order.sparmeduser': {
            'Meta': {'object_name': 'SparmedUser'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_person_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_telephone': ('django.db.models.fields.IntegerField', [], {'max_length': '20', 'unique': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'postal_code': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['online_order']