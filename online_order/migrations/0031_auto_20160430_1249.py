# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0030_order_chosen_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='chosen_currency',
            field=models.CharField(choices=[('EUR', 'Euro'), ('USD', 'US Dollars'), ('Both', 'Both')], max_length=255, verbose_name='Choose the currency of the invoice', blank=True, null=True),
        ),
    ]
