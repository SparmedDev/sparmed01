# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0025_sparmeduser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparmeduser',
            name='date_joined',
            field=models.DateTimeField(verbose_name='Date joined', null=True, blank=True, default=django.utils.timezone.now),
        ),
    ]
