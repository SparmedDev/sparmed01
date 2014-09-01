# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Order.aircleaner_instructions'
        db.alter_column(u'online_order_order', 'aircleaner_instructions', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))
        # Adding field 'SparmedUser.orders'
        db.add_column(u'online_order_sparmeduser', 'orders',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['online_order.Order'], blank=True, related_name='orders'),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'Order.aircleaner_instructions'
        db.alter_column(u'online_order_order', 'aircleaner_instructions', self.gf('django.db.models.fields.CharField')(max_length=2))
        # Deleting field 'SparmedUser.orders'
        db.delete_column(u'online_order_sparmeduser', 'orders_id')


    models = {
        u'online_order.order': {
            'Meta': {'object_name': 'Order', 'ordering': "['-date']"},
            'account_no': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'aircleaner_instructions': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'arranged_freight': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'documents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'freight_forwarder': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance_desired': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'invoice_company_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'invoice_company_country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'invoice_company_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'invoice_company_postal_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'other_remarks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'packing_instructions': ('django.db.models.fields.CharField', [], {'max_length': '2', 'default': "'EP'"}),
            'packing_remarks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'shipping_and_invoice_same': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
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
            'orders': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': u"orm['online_order.Order']", 'blank': 'True', 'related_name': "'orders'"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'postal_code': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['online_order']