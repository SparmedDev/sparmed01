# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0026_auto_20151213_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sparmeduser',
            name='is_staff',
        ),
    ]
