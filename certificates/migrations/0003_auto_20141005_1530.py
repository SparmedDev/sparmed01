# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0002_auto_20141005_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificatesubgroup',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Subgroup Title/Name', blank=True),
        ),
    ]
