# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0016_auto_20150822_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparmeduser',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Sparmed Client No.'),
        ),
    ]
