# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0011_auto_20150301_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparmeduser',
            name='last_login',
            field=models.DateTimeField(blank=True, verbose_name='last login', null=True),
        ),
    ]
