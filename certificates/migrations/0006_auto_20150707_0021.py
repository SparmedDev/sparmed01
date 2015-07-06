# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0005_auto_20150706_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificategroup',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='certificategroup',
            name='title_es',
        ),
        migrations.RemoveField(
            model_name='certificategroup',
            name='title_pt_br',
        ),
        migrations.RemoveField(
            model_name='certificategroup',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='certificateitem',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='certificateitem',
            name='title_es',
        ),
        migrations.RemoveField(
            model_name='certificateitem',
            name='title_pt_br',
        ),
        migrations.RemoveField(
            model_name='certificateitem',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='certificatesubgroup',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='certificatesubgroup',
            name='title_es',
        ),
        migrations.RemoveField(
            model_name='certificatesubgroup',
            name='title_pt_br',
        ),
        migrations.RemoveField(
            model_name='certificatesubgroup',
            name='title_ru',
        ),
    ]
