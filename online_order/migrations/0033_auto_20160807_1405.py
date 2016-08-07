# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0032_auto_20160430_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparmeduser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user is regarded as staff'),
        ),
    ]
