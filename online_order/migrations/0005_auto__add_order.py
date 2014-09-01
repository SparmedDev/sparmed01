# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Order'
        db.create_table(u'online_order_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('arranged_freight', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('freight_forwarder', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True, null=True)),
            ('account_no', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True, null=True)),
            ('packing_instructions', self.gf('django.db.models.fields.CharField')(max_length=2, default='EP')),
            ('packing_remarks', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('aircleaner_instructions', self.gf('django.db.models.fields.CharField')(max_length=2, default='CB')),
            ('insurance_desired', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('documents', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('shipping_and_invoice_same', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('invoice_company_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True, null=True)),
            ('invoice_company_address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True, null=True)),
            ('invoice_company_postal_code', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('invoice_company_country', self.gf('django_countries.fields.CountryField')(max_length=2, blank=True, null=True)),
            ('other_remarks', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'online_order', ['Order'])


    def backwards(self, orm):
        # Deleting model 'Order'
        db.delete_table(u'online_order_order')


    models = {
        u'online_order.order': {
            'Meta': {'object_name': 'Order', 'ordering': "['-date']"},
            'account_no': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'aircleaner_instructions': ('django.db.models.fields.CharField', [], {'max_length': '2', 'default': "'CB'"}),
            'arranged_freight': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'documents': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'freight_forwarder': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance_desired': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'invoice_company_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'invoice_company_country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'blank': 'True', 'null': 'True'}),
            'invoice_company_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
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
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'postal_code': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['online_order']