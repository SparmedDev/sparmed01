# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_auto_20150707_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='image_hires',
            field=sorl.thumbnail.fields.ImageField(null=True, blank=True, upload_to=b'/media/products'),
        ),
        migrations.AddField(
            model_name='shopimage',
            name='image_hires',
            field=sorl.thumbnail.fields.ImageField(null=True, blank=True, upload_to=b'/media/products/'),
        ),
    ]
