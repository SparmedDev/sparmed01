# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0005_auto_20141005_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparmeduser',
            name='postal_code',
            field=models.CharField(max_length=255, blank=True, verbose_name=b'Company Postal Code', null=True),
        ),
    ]
