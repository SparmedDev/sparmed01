# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0013_auto_20150710_0148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sparmeduser',
            options={'verbose_name_plural': 'users', 'verbose_name': 'user'},
        ),
        migrations.AddField(
            model_name='sparmeduser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='sparmeduser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'),
        ),
    ]
