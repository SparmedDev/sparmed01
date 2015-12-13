# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0028_sparmeduser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sparmeduser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='sparmeduser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='sparmeduser',
            name='username',
        ),
    ]
