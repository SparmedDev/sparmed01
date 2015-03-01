# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20141004_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name=b'Write your news post here (Please do not attempt to insert images here, instead use the news image below)'),
            preserve_default=True,
        ),
    ]
