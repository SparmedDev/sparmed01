# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20150301_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='long_text',
            field=ckeditor.fields.RichTextField(null=True, verbose_name=b'Product Long Text', blank=True),
            preserve_default=True,
        ),
    ]
