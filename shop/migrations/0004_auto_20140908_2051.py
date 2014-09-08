# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20140908_2008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories', 'ordering': ['-order_index']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-order_index']},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'Subcategories', 'ordering': ['-order_index']},
        ),
        migrations.AddField(
            model_name='category',
            name='order_index',
            field=models.PositiveIntegerField(blank=True, null=True, default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='order_index',
            field=models.PositiveIntegerField(blank=True, null=True, default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='order_index',
            field=models.PositiveIntegerField(blank=True, null=True, default=0),
            preserve_default=True,
        ),
    ]
