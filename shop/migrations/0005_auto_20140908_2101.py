# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20140908_2051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories', 'ordering': ['order_index']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['order_index']},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'Subcategories', 'ordering': ['order_index']},
        ),
    ]
