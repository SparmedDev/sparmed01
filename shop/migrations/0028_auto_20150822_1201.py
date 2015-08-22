# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_auto_20150719_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(max_length=255, default=b'OOOO-0000', verbose_name='Order No.'),
        ),
    ]
