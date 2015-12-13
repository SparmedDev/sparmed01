# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0018_auto_20151210_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparmeduser',
            name='address',
            field=models.CharField(blank=True, verbose_name=b'Company Address', max_length=255),
        ),
        migrations.AlterField(
            model_name='sparmeduser',
            name='city',
            field=models.CharField(blank=True, verbose_name='Company City', max_length=255),
        ),
        migrations.AlterField(
            model_name='sparmeduser',
            name='company_name',
            field=models.CharField(blank=True, verbose_name=b'Company Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='sparmeduser',
            name='contact_person_name',
            field=models.CharField(blank=True, verbose_name='Company Contact Person Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='sparmeduser',
            name='contact_telephone',
            field=models.CharField(blank=True, verbose_name='Contact Telephone Number', max_length=50),
        ),
        migrations.AlterField(
            model_name='sparmeduser',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]
