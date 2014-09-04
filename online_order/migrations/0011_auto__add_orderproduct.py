# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrderProduct'
        db.create_table(u'online_order_orderproduct', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('product_id', self.gf('django.db.models.fields.CharField')(max_length=255, default='OOOO-0000')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, default='Product 1')),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('order_history', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['online_order.OrderHistoryItem'], related_name='items')),
        ))
        db.send_create_signal(u'online_order', ['OrderProduct'])

        # Removing M2M table for field items on 'OrderHistoryItem'
        db.delete_table(db.shorten_name(u'online_order_orderhistoryitem_items'))


    def backwards(self, orm):
        # Deleting model 'OrderProduct'
        db.delete_table(u'online_order_orderproduct')

        # Adding M2M table for field items on 'OrderHistoryItem'
        m2m_table_name = db.shorten_name(u'online_order_orderhistoryitem_items')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orderhistoryitem', models.ForeignKey(orm[u'online_order.orderhistoryitem'], null=False)),
            ('item', models.ForeignKey(orm[u'cart.item'], null=False))
        ))
        db.create_unique(m2m_table_name, ['orderhistoryitem_id', 'item_id'])


    models = {
        u'online_order.order': {
            'Meta': {'object_name': 'Order', 'ordering': "['-date']"},
            'account_no': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'aircleaner_instructions': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '2'}),
            'arranged_freight': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'documents': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'freight_forwarder': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance_desired': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'invoice_company_address': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'invoice_company_country': ('django_countries.fields.CountryField', [], {'blank': 'True', 'null': 'True', 'max_length': '2'}),
            'invoice_company_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'invoice_company_postal_code': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'other_remarks': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'packing_instructions': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '2', 'default': "'EP'"}),
            'packing_remarks': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'shipping_and_invoice_same': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'online_order.orderhistoryitem': {
            'Meta': {'_ormbases': [u'online_order.Order'], 'object_name': 'OrderHistoryItem', 'ordering': "['-date']"},
            u'order_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['online_order.Order']", 'unique': 'True', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': u"orm['online_order.SparmedUser']", 'related_name': "'orders'"})
        },
        u'online_order.orderproduct': {
            'Meta': {'object_name': 'OrderProduct'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'Product 1'"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order_history': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['online_order.OrderHistoryItem']", 'related_name': "'items'"}),
            'product_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'OOOO-0000'"}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
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