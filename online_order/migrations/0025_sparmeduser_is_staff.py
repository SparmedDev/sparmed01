# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0024_remove_sparmeduser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparmeduser',
            name='is_staff',
            field=models.BooleanField(help_text='Designates whether the user is regarded as staff', default=True),
        ),
    ]
