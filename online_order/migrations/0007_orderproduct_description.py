# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0006_auto_20141006_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='description',
            field=models.CharField(blank=True, verbose_name=b'Product Long Name', max_length=255, null=True),
            preserve_default=True,
        ),
    ]
