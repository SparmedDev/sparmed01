# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0003_auto_20150103_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distributor',
            name='name',
        ),
    ]
