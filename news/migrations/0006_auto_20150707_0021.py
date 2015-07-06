# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20150706_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsimage',
            name='image_title_en',
        ),
        migrations.RemoveField(
            model_name='newsimage',
            name='image_title_es',
        ),
        migrations.RemoveField(
            model_name='newsimage',
            name='image_title_pt_br',
        ),
        migrations.RemoveField(
            model_name='newsimage',
            name='image_title_ru',
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='content_en',
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='content_es',
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='content_pt_br',
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='content_ru',
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='title_es',
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='title_pt_br',
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='title_ru',
        ),
    ]
