# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributor',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]
