# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name=b'Write your news post here (Please do not attempt to insert images here, instead use the news image below)'),
        ),
    ]
