# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_newsimage_image_hires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsimage',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'media/news/'),
        ),
        migrations.AlterField(
            model_name='newsimage',
            name='image_hires',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'media/news/', blank=True, null=True),
        ),
    ]
