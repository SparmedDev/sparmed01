# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0004_order_arranged_packing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='arranged_packing',
            field=models.BooleanField(default=True, verbose_name=b'SparMED Arranges Packaging?'),
        ),
    ]
