# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_shopimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopimage',
            name='category',
            field=models.ForeignKey(related_name=b'images', to='shop.Category', verbose_name=b'Associated Category', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='shopimage',
            name='subcategory',
            field=models.ForeignKey(related_name=b'images', to='shop.Subcategory', verbose_name=b'Associated Subcategory', null=True, blank=True),
        ),
    ]
