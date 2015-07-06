# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20150707_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(verbose_name='Category Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='short_name',
            field=models.CharField(verbose_name='Category Short Name (for navigation bar)', max_length=40),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(verbose_name='Product Short Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(verbose_name='Subcategory Name', max_length=255),
        ),
    ]
