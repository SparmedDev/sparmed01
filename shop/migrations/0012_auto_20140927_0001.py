# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20140926_1940'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['order_index', 'added']},
        ),
    ]
