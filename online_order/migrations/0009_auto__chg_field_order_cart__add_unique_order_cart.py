# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Order.cart'
        db.alter_column(u'online_order_order', 'cart_id', self.gf('django.db.models.fields.related.OneToOneField')(null=True, unique=True, to=orm['cart.Cart']))
        # Adding unique constraint on 'Order', fields ['cart']
        db.create_unique(u'online_order_order', ['cart_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Order', fields ['cart']
        db.delete_unique(u'online_order_order', ['cart_id'])


        # Changing field 'Order.cart'
        db.alter_column(u'online_order_order', 'cart_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cart.Cart'], null=True))

    models = {
        u'cart.cart': {
            'Meta': {'object_name': 'Cart', 'ordering': "('-creation_date',)"},
            'checked_out': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'online_order.order': {
            'Meta': {'object_name': 'Order', 'ordering': "['-date']"},
            'account_no': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'aircleaner_instructions': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'arranged_freight': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cart': ('django.db.models.fields.related.OneToOneField', [], {'null': 'True', 'blank': 'True', 'related_name': "'order'", 'unique': 'True', 'to': u"orm['cart.Cart']"}),
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
            'packing_instructions': ('django.db.models.fields.CharField', [], {'max_length': '2', 'default': "'EP'"}),
            'packing_remarks': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'shipping_and_invoice_same': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'orders'", 'null': 'True', 'to': u"orm['online_order.SparmedUser']"})
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