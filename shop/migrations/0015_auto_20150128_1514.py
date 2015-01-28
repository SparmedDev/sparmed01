# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20150128_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='color',
            field=colorfield.fields.ColorField(verbose_name=b'Subcategory Color', max_length=10, default=b'008393'),
        ),
    ]
