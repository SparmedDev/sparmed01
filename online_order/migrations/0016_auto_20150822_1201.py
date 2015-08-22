# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0015_auto_20150710_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='product_id',
            field=models.CharField(max_length=255, default=b'OOOO-0000', verbose_name='Order No.'),
        ),
    ]
