# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0002_auto_20150103_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributor',
            name='country',
            field=models.CharField(verbose_name=b'Country Name', max_length=255),
        ),
    ]
