# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0003_auto_20141004_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='arranged_packing',
            field=models.BooleanField(help_text=b'Please note if SparMED arranges packaging, we will choose the best and safest way of packing your order', verbose_name=b'SparMED Arranges Packaging?', default=True),
            preserve_default=True,
        ),
    ]
