# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_auto_20150920_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='get_stock_numbers',
            field=models.BooleanField(verbose_name='Automatically Get Stock Numbers from E-conomics for this Category', default=False),
        ),
    ]
