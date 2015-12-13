# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0023_auto_20151210_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sparmeduser',
            name='is_staff',
        ),
    ]
