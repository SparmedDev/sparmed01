# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0022_auto_20151210_1217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sparmeduser',
            old_name='is_straff',
            new_name='is_staff',
        ),
    ]
