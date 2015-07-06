# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20150707_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=models.CharField(null=True, blank=True, verbose_name='Category description', max_length=255),
        ),
        migrations.AddField(
            model_name='category',
            name='description_es',
            field=models.CharField(null=True, blank=True, verbose_name='Category description', max_length=255),
        ),
        migrations.AddField(
            model_name='category',
            name='description_pt_br',
            field=models.CharField(null=True, blank=True, verbose_name='Category description', max_length=255),
        ),
        migrations.AddField(
            model_name='category',
            name='description_ru',
            field=models.CharField(null=True, blank=True, verbose_name='Category description', max_length=255),
        ),
        migrations.AddField(
            model_name='category',
            name='long_text_en',
            field=ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Category Long Text (Please do not insert images!)'),
        ),
        migrations.AddField(
            model_name='category',
            name='long_text_es',
            field=ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Category Long Text (Please do not insert images!)'),
        ),
        migrations.AddField(
            model_name='category',
            name='long_text_pt_br',
            field=ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Category Long Text (Please do not insert images!)'),
        ),
        migrations.AddField(
            model_name='category',
            name='long_text_ru',
            field=ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Category Long Text (Please do not insert images!)'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(null=True, verbose_name='Category Name', max_length=255),
        ),
        migrations.AddField(
            model_name='category',
            name='name_es',
            field=models.CharField(null=True, verbose_name='Category Name', max_length=255),
        ),
        migrations.AddField(
            model_name='category',
            name='name_pt_br',
            field=models.CharField(null=True, verbose_name='Category Name', max_length=255),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(null=True, verbose_name='Category Name', max_length=255),
        ),
        migrations.AddField(
            model_name='category',
            name='short_name_en',
            field=models.CharField(null=True, verbose_name='Category Short Name (for navigation bar)', max_length=40),
        ),
        migrations.AddField(
            model_name='category',
            name='short_name_es',
            field=models.CharField(null=True, verbose_name='Category Short Name (for navigation bar)', max_length=40),
        ),
        migrations.AddField(
            model_name='category',
            name='short_name_pt_br',
            field=models.CharField(null=True, verbose_name='Category Short Name (for navigation bar)', max_length=40),
        ),
        migrations.AddField(
            model_name='category',
            name='short_name_ru',
            field=models.CharField(null=True, verbose_name='Category Short Name (for navigation bar)', max_length=40),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.CharField(null=True, blank=True, verbose_name='Product Description', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='description_es',
            field=models.CharField(null=True, blank=True, verbose_name='Product Description', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='description_pt_br',
            field=models.CharField(null=True, blank=True, verbose_name='Product Description', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.CharField(null=True, blank=True, verbose_name='Product Description', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='long_name_en',
            field=models.CharField(null=True, blank=True, verbose_name='Product Long Name', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='long_name_es',
            field=models.CharField(null=True, blank=True, verbose_name='Product Long Name', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='long_name_pt_br',
            field=models.CharField(null=True, blank=True, verbose_name='Product Long Name', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='long_name_ru',
            field=models.CharField(null=True, blank=True, verbose_name='Product Long Name', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='long_text_en',
            field=ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Product Long Text'),
        ),
        migrations.AddField(
            model_name='product',
            name='long_text_es',
            field=ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Product Long Text'),
        ),
        migrations.AddField(
            model_name='product',
            name='long_text_pt_br',
            field=ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Product Long Text'),
        ),
        migrations.AddField(
            model_name='product',
            name='long_text_ru',
            field=ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Product Long Text'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(null=True, verbose_name='Product Short Name', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='name_es',
            field=models.CharField(null=True, verbose_name='Product Short Name', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='name_pt_br',
            field=models.CharField(null=True, verbose_name='Product Short Name', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(null=True, verbose_name='Product Short Name', max_length=100),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_title_en',
            field=models.CharField(null=True, blank=True, verbose_name='Picture Title', max_length=200),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_title_es',
            field=models.CharField(null=True, blank=True, verbose_name='Picture Title', max_length=200),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_title_pt_br',
            field=models.CharField(null=True, blank=True, verbose_name='Picture Title', max_length=200),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_title_ru',
            field=models.CharField(null=True, blank=True, verbose_name='Picture Title', max_length=200),
        ),
        migrations.AddField(
            model_name='shopimage',
            name='image_title_en',
            field=models.CharField(null=True, blank=True, verbose_name='Picture Title', max_length=255),
        ),
        migrations.AddField(
            model_name='shopimage',
            name='image_title_es',
            field=models.CharField(null=True, blank=True, verbose_name='Picture Title', max_length=255),
        ),
        migrations.AddField(
            model_name='shopimage',
            name='image_title_pt_br',
            field=models.CharField(null=True, blank=True, verbose_name='Picture Title', max_length=255),
        ),
        migrations.AddField(
            model_name='shopimage',
            name='image_title_ru',
            field=models.CharField(null=True, blank=True, verbose_name='Picture Title', max_length=255),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description_en',
            field=models.CharField(null=True, blank=True, verbose_name='Subcategory description', max_length=255),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description_es',
            field=models.CharField(null=True, blank=True, verbose_name='Subcategory description', max_length=255),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description_pt_br',
            field=models.CharField(null=True, blank=True, verbose_name='Subcategory description', max_length=255),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description_ru',
            field=models.CharField(null=True, blank=True, verbose_name='Subcategory description', max_length=255),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='long_text_en',
            field=ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Subcategory Long Text (Please do not insert images!)'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='long_text_es',
            field=ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Subcategory Long Text (Please do not insert images!)'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='long_text_pt_br',
            field=ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Subcategory Long Text (Please do not insert images!)'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='long_text_ru',
            field=ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='Subcategory Long Text (Please do not insert images!)'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_en',
            field=models.CharField(null=True, verbose_name='Subcategory Name', max_length=255),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_es',
            field=models.CharField(null=True, verbose_name='Subcategory Name', max_length=255),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_pt_br',
            field=models.CharField(null=True, verbose_name='Subcategory Name', max_length=255),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_ru',
            field=models.CharField(null=True, verbose_name='Subcategory Name', max_length=255),
        ),
    ]
