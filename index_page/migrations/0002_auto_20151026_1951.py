# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpagemodel',
            name='slogan_en',
            field=models.CharField(null=True, blank=True, verbose_name='Index Page Slogan', max_length=255),
        ),
        migrations.AddField(
            model_name='indexpagemodel',
            name='slogan_es',
            field=models.CharField(null=True, blank=True, verbose_name='Index Page Slogan', max_length=255),
        ),
        migrations.AddField(
            model_name='indexpagemodel',
            name='slogan_pt_br',
            field=models.CharField(null=True, blank=True, verbose_name='Index Page Slogan', max_length=255),
        ),
        migrations.AddField(
            model_name='indexpagemodel',
            name='slogan_ru',
            field=models.CharField(null=True, blank=True, verbose_name='Index Page Slogan', max_length=255),
        ),
    ]
