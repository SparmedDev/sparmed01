# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20150707_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsimage',
            name='image_title_en',
            field=models.CharField(null=True, blank=True, verbose_name='Picture Title', max_length=200),
        ),
        migrations.AddField(
            model_name='newsimage',
            name='image_title_es',
            field=models.CharField(null=True, blank=True, verbose_name='Picture Title', max_length=200),
        ),
        migrations.AddField(
            model_name='newsimage',
            name='image_title_pt_br',
            field=models.CharField(null=True, blank=True, verbose_name='Picture Title', max_length=200),
        ),
        migrations.AddField(
            model_name='newsimage',
            name='image_title_ru',
            field=models.CharField(null=True, blank=True, verbose_name='Picture Title', max_length=200),
        ),
        migrations.AddField(
            model_name='newspost',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Write your news post here (Please do not attempt to insert images here, instead use the news image below)'),
        ),
        migrations.AddField(
            model_name='newspost',
            name='content_es',
            field=ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Write your news post here (Please do not attempt to insert images here, instead use the news image below)'),
        ),
        migrations.AddField(
            model_name='newspost',
            name='content_pt_br',
            field=ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Write your news post here (Please do not attempt to insert images here, instead use the news image below)'),
        ),
        migrations.AddField(
            model_name='newspost',
            name='content_ru',
            field=ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Write your news post here (Please do not attempt to insert images here, instead use the news image below)'),
        ),
        migrations.AddField(
            model_name='newspost',
            name='title_en',
            field=models.CharField(null=True, max_length=60),
        ),
        migrations.AddField(
            model_name='newspost',
            name='title_es',
            field=models.CharField(null=True, max_length=60),
        ),
        migrations.AddField(
            model_name='newspost',
            name='title_pt_br',
            field=models.CharField(null=True, max_length=60),
        ),
        migrations.AddField(
            model_name='newspost',
            name='title_ru',
            field=models.CharField(null=True, max_length=60),
        ),
    ]
