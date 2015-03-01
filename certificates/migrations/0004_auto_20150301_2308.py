# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0003_auto_20141005_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificategroup',
            name='added',
            field=models.DateTimeField(verbose_name=b'Date and time added', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='certificateitem',
            name='added',
            field=models.DateTimeField(verbose_name=b'Date and time added', default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='certificatesubgroup',
            name='added',
            field=models.DateTimeField(verbose_name=b'Date and time added', default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
