# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0002_auto_20140929_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparmeduser',
            name='postal_code',
            field=models.IntegerField(null=True, verbose_name=b'Company Postal Code', blank=True),
        ),
    ]
