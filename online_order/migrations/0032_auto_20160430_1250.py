# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0031_auto_20160430_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='chosen_currency',
            field=models.CharField(default=b'EUR', max_length=255, blank=True, verbose_name='Choose the currency of the invoice', choices=[('EUR', 'Euro'), ('USD', 'US Dollars'), ('Both', 'Both')]),
        ),
    ]
