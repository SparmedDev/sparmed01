# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0006_auto_20150707_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificategroup',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name='Group Title/Name', null=True),
        ),
        migrations.AddField(
            model_name='certificategroup',
            name='title_es',
            field=models.CharField(max_length=255, verbose_name='Group Title/Name', null=True),
        ),
        migrations.AddField(
            model_name='certificategroup',
            name='title_pt_br',
            field=models.CharField(max_length=255, verbose_name='Group Title/Name', null=True),
        ),
        migrations.AddField(
            model_name='certificategroup',
            name='title_ru',
            field=models.CharField(max_length=255, verbose_name='Group Title/Name', null=True),
        ),
        migrations.AddField(
            model_name='certificateitem',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name='Certificate/Document Title', null=True),
        ),
        migrations.AddField(
            model_name='certificateitem',
            name='title_es',
            field=models.CharField(max_length=255, verbose_name='Certificate/Document Title', null=True),
        ),
        migrations.AddField(
            model_name='certificateitem',
            name='title_pt_br',
            field=models.CharField(max_length=255, verbose_name='Certificate/Document Title', null=True),
        ),
        migrations.AddField(
            model_name='certificateitem',
            name='title_ru',
            field=models.CharField(max_length=255, verbose_name='Certificate/Document Title', null=True),
        ),
        migrations.AddField(
            model_name='certificatesubgroup',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name='Subgroup Title/Name', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='certificatesubgroup',
            name='title_es',
            field=models.CharField(max_length=255, verbose_name='Subgroup Title/Name', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='certificatesubgroup',
            name='title_pt_br',
            field=models.CharField(max_length=255, verbose_name='Subgroup Title/Name', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='certificatesubgroup',
            name='title_ru',
            field=models.CharField(max_length=255, verbose_name='Subgroup Title/Name', blank=True, null=True),
        ),
    ]
