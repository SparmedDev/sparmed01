# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='color',
            field=colorfield.fields.ColorField(null=True, verbose_name=b'Subcategory Color', max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
