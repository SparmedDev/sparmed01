# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0008_auto_20150707_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificategroup',
            name='title_en',
            field=models.CharField(null=True, verbose_name='Group Title/Name', max_length=255),
        ),
        migrations.AddField(
            model_name='certificategroup',
            name='title_es',
            field=models.CharField(null=True, verbose_name='Group Title/Name', max_length=255),
        ),
        migrations.AddField(
            model_name='certificategroup',
            name='title_pt_br',
            field=models.CharField(null=True, verbose_name='Group Title/Name', max_length=255),
        ),
        migrations.AddField(
            model_name='certificategroup',
            name='title_ru',
            field=models.CharField(null=True, verbose_name='Group Title/Name', max_length=255),
        ),
        migrations.AddField(
            model_name='certificateitem',
            name='title_en',
            field=models.CharField(null=True, verbose_name='Certificate/Document Title', max_length=255),
        ),
        migrations.AddField(
            model_name='certificateitem',
            name='title_es',
            field=models.CharField(null=True, verbose_name='Certificate/Document Title', max_length=255),
        ),
        migrations.AddField(
            model_name='certificateitem',
            name='title_pt_br',
            field=models.CharField(null=True, verbose_name='Certificate/Document Title', max_length=255),
        ),
        migrations.AddField(
            model_name='certificateitem',
            name='title_ru',
            field=models.CharField(null=True, verbose_name='Certificate/Document Title', max_length=255),
        ),
        migrations.AddField(
            model_name='certificatesubgroup',
            name='title_en',
            field=models.CharField(null=True, blank=True, verbose_name='Subgroup Title/Name', max_length=255),
        ),
        migrations.AddField(
            model_name='certificatesubgroup',
            name='title_es',
            field=models.CharField(null=True, blank=True, verbose_name='Subgroup Title/Name', max_length=255),
        ),
        migrations.AddField(
            model_name='certificatesubgroup',
            name='title_pt_br',
            field=models.CharField(null=True, blank=True, verbose_name='Subgroup Title/Name', max_length=255),
        ),
        migrations.AddField(
            model_name='certificatesubgroup',
            name='title_ru',
            field=models.CharField(null=True, blank=True, verbose_name='Subgroup Title/Name', max_length=255),
        ),
    ]
