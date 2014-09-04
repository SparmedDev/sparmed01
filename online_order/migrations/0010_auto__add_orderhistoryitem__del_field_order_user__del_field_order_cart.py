# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrderHistoryItem'
        db.create_table(u'online_order_orderhistoryitem', (
            (u'order_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['online_order.Order'], unique=True, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['online_order.SparmedUser'], related_name='orders')),
        ))
        db.send_create_signal(u'online_order', ['OrderHistoryItem'])

        # Adding M2M table for field items on 'OrderHistoryItem'
        m2m_table_name = db.shorten_name(u'online_order_orderhistoryitem_items')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orderhistoryitem', models.ForeignKey(orm[u'online_order.orderhistoryitem'], null=False)),
            ('item', models.ForeignKey(orm[u'cart.item'], null=False))
        ))
        db.create_unique(m2m_table_name, ['orderhistoryitem_id', 'item_id'])

        # Deleting field 'Order.user'
        db.delete_column(u'online_order_order', 'user_id')

        # Deleting field 'Order.cart'
        db.delete_column(u'online_order_order', 'cart_id')


    def backwards(self, orm):
        # Deleting model 'OrderHistoryItem'
        db.delete_table(u'online_order_orderhistoryitem')

        # Removing M2M table for field items on 'OrderHistoryItem'
        db.delete_table(db.shorten_name(u'online_order_orderhistoryitem_items'))

        # Adding field 'Order.user'
        db.add_column(u'online_order_order', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['online_order.SparmedUser'], related_name='orders'),
                      keep_default=False)

        # Adding field 'Order.cart'
        db.add_column(u'online_order_order', 'cart',
                      self.gf('django.db.models.fields.related.OneToOneField')(null=True, related_name='order', to=orm['cart.Cart'], unique=True, blank=True),
                      keep_default=False)


    models = {
        u'cart.cart': {
            'Meta': {'object_name': 'Cart', 'ordering': "('-creation_date',)"},
            'checked_out': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'cart.item': {
            'Meta': {'object_name': 'Item', 'ordering': "('cart',)"},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cart.Cart']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'online_order.order': {
            'Meta': {'object_name': 'Order', 'ordering': "['-date']"},
            'account_no': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'aircleaner_instructions': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'arranged_freight': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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
            'packing_instructions': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '2', 'default': "'EP'"}),
            'packing_remarks': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'shipping_and_invoice_same': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'online_order.orderhistoryitem': {
            'Meta': {'_ormbases': [u'online_order.Order'], 'object_name': 'OrderHistoryItem', 'ordering': "['-date']"},
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'blank': 'True', 'to': u"orm['cart.Item']", 'symmetrical': 'False'}),
            u'order_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['online_order.Order']", 'unique': 'True', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': u"orm['online_order.SparmedUser']", 'related_name': "'orders'"})
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