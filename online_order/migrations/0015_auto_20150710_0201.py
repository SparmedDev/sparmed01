# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0014_auto_20150710_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparmeduser',
            name='is_admin',
            field=models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False),
        ),
    ]
