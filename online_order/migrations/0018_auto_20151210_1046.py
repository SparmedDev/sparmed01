# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0017_auto_20151011_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparmeduser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True, verbose_name='Date joined'),
        ),
        migrations.AlterField(
            model_name='sparmeduser',
            name='is_active',
            field=models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='Active', default=True),
        ),
    ]
