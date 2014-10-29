# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0008_auto_20141016_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparmeduser',
            name='contact_telephone',
            field=models.CharField(max_length=50, verbose_name=b'Contact Telephone Number'),
        ),
    ]
