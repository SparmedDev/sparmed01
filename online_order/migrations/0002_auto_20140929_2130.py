# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='packing_instructions',
            field=models.CharField(help_text=b'Please note if nothing is filled out SparMED will choose the best and safest way of packing your order.', verbose_name=b'Packaging Instructions', max_length=2, blank=True, default=b'EP', choices=[(b'EP', b'Euro Pallet'), (b'HP', b'Half Pallet'), (b'BX', b'Box')]),
        ),
    ]
