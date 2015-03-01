# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0010_auto_20150216_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(verbose_name=b'Date and time of order', default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
