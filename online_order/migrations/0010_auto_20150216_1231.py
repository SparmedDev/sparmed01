# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0009_auto_20141029_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='long_name',
            field=models.CharField(verbose_name=b'Product Long Name', null=True, max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='description',
            field=models.CharField(verbose_name=b'Product Description', null=True, max_length=255, blank=True),
        ),
    ]
