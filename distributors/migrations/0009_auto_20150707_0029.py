# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0008_auto_20150707_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributor',
            name='country_en',
            field=models.CharField(null=True, verbose_name='Country Name', max_length=255),
        ),
        migrations.AddField(
            model_name='distributor',
            name='country_es',
            field=models.CharField(null=True, verbose_name='Country Name', max_length=255),
        ),
        migrations.AddField(
            model_name='distributor',
            name='country_pt_br',
            field=models.CharField(null=True, verbose_name='Country Name', max_length=255),
        ),
        migrations.AddField(
            model_name='distributor',
            name='country_ru',
            field=models.CharField(null=True, verbose_name='Country Name', max_length=255),
        ),
    ]
