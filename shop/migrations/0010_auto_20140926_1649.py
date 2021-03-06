# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20140919_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(null=True, verbose_name=b'Size (LxDxH)', blank=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.CharField(null=True, verbose_name=b'Weight', blank=True, max_length=255),
            preserve_default=True,
        ),
    ]
