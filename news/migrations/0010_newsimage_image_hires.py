# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20150707_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsimage',
            name='image_hires',
            field=sorl.thumbnail.fields.ImageField(null=True, blank=True, upload_to=b'/media/news'),
        ),
    ]
