# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_order', '0021_auto_20151210_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparmeduser',
            name='first_name',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='sparmeduser',
            name='is_straff',
            field=models.BooleanField(help_text='Designates whether the user is regarded as staff', default=False),
        ),
        migrations.AddField(
            model_name='sparmeduser',
            name='last_name',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='sparmeduser',
            name='username',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
    ]
