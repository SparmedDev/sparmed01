# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20150216_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='long_text',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name=b'Category Long Text (Please do not insert images!)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='long_text',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name=b'Subcategory Long Text (Please do not insert images!)'),
            preserve_default=True,
        ),
    ]
