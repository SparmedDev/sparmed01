# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0020_auto_20151210_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sparmeduser',
            name='is_staff',
        ),
        migrations.AlterField(
            model_name='sparmeduser',
            name='date_joined',
            field=models.DateTimeField(verbose_name='Date joined', blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='sparmeduser',
            name='email',
            field=models.EmailField(verbose_name='Contact Email Address', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='sparmeduser',
            name='is_active',
            field=models.BooleanField(verbose_name='Active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True),
        ),
    ]
