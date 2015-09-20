# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import validatedfile.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_auto_20150822_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='document',
            field=validatedfile.fields.ValidatedFileField(verbose_name='PDF Document file (56 MB max)', blank=True, null=True, upload_to=b'documents/'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'media/products/'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image_hires',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'media/products/', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shopimage',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'media/products/'),
        ),
        migrations.AlterField(
            model_name='shopimage',
            name='image_hires',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'media/products/', blank=True, null=True),
        ),
    ]
