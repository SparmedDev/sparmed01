# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0029_auto_20151213_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='chosen_currency',
            field=models.CharField(verbose_name='Choose the currency of the invoice', choices=[('EUR', 'Euro'), ('USD', 'US Dollars'), ('Both', 'Both')], max_length=4, blank=True, null=True),
        ),
    ]
