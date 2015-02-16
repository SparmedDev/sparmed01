# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20150128_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='long_name',
            field=models.CharField(verbose_name=b'Product Long Name', null=True, max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(verbose_name=b'Product Description', blank=True, max_length=255),
        ),
    ]
