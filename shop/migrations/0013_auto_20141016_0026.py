# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20140927_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='hs_code',
            field=models.CharField(verbose_name=b'Tariff No. / HS Code', blank=True, max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='hs_code',
            field=models.CharField(verbose_name=b'Tariff No. / HS Code', blank=True, max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='hs_code',
            field=models.CharField(verbose_name=b'Tariff No. / HS Code', blank=True, max_length=255, null=True),
            preserve_default=True,
        ),
    ]
