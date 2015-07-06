# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0006_auto_20150707_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributor',
            name='country_en',
            field=models.CharField(max_length=255, verbose_name='Country Name', null=True),
        ),
        migrations.AddField(
            model_name='distributor',
            name='country_es',
            field=models.CharField(max_length=255, verbose_name='Country Name', null=True),
        ),
        migrations.AddField(
            model_name='distributor',
            name='country_pt_br',
            field=models.CharField(max_length=255, verbose_name='Country Name', null=True),
        ),
        migrations.AddField(
            model_name='distributor',
            name='country_ru',
            field=models.CharField(max_length=255, verbose_name='Country Name', null=True),
        ),
    ]
