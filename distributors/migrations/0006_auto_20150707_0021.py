# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributors', '0005_auto_20150706_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distributor',
            name='country_en',
        ),
        migrations.RemoveField(
            model_name='distributor',
            name='country_es',
        ),
        migrations.RemoveField(
            model_name='distributor',
            name='country_pt_br',
        ),
        migrations.RemoveField(
            model_name='distributor',
            name='country_ru',
        ),
    ]
