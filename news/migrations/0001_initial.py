# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewsImage'
        db.create_table(u'news_newsimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_title', self.gf('django.db.models.fields.CharField')(blank=True, max_length=200)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('news_post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['news.NewsPost'])),
        ))
        db.send_create_signal(u'news', ['NewsImage'])

        # Adding model 'NewsPost'
        db.create_table(u'news_newspost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('content', self.gf('django.db.models.fields.TextField')(default='Write your news post here')),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'news', ['NewsPost'])


    def backwards(self, orm):
        # Deleting model 'NewsImage'
        db.delete_table(u'news_newsimage')

        # Deleting model 'NewsPost'
        db.delete_table(u'news_newspost')


    models = {
        u'news.newsimage': {
            'Meta': {'object_name': 'NewsImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'image_title': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '200'}),
            'news_post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['news.NewsPost']"})
        },
        u'news.newspost': {
            'Meta': {'object_name': 'NewsPost', 'ordering': "['-added']"},
            'added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "'Write your news post here'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['news']