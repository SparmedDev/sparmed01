# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150301_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='added',
            field=models.DateTimeField(verbose_name=b'Date and time added', default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
