# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0019_auto_20151210_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparmeduser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='sparmeduser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='sparmeduser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, db_index=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='sparmeduser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active.  Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]
