# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20140908_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='short_name',
            field=models.CharField(verbose_name=b'Category Short Name (for navigation bar)', max_length=40, default=b'Cat1'),
        ),
    ]
