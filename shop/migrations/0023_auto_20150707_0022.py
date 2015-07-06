# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_auto_20150707_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=models.CharField(max_length=255, verbose_name='Category description', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_es',
            field=models.CharField(max_length=255, verbose_name='Category description', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_pt_br',
            field=models.CharField(max_length=255, verbose_name='Category description', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_ru',
            field=models.CharField(max_length=255, verbose_name='Category description', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='long_text_en',
            field=ckeditor.fields.RichTextField(verbose_name='Category Long Text (Please do not insert images!)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='long_text_es',
            field=ckeditor.fields.RichTextField(verbose_name='Category Long Text (Please do not insert images!)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='long_text_pt_br',
            field=ckeditor.fields.RichTextField(verbose_name='Category Long Text (Please do not insert images!)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='long_text_ru',
            field=ckeditor.fields.RichTextField(verbose_name='Category Long Text (Please do not insert images!)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(default=b'Category 1', max_length=255, verbose_name='Category Name', null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_es',
            field=models.CharField(default=b'Category 1', max_length=255, verbose_name='Category Name', null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_pt_br',
            field=models.CharField(default=b'Category 1', max_length=255, verbose_name='Category Name', null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(default=b'Category 1', max_length=255, verbose_name='Category Name', null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='short_name_en',
            field=models.CharField(default=b'Cat1', max_length=40, verbose_name='Category Short Name (for navigation bar)', null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='short_name_es',
            field=models.CharField(default=b'Cat1', max_length=40, verbose_name='Category Short Name (for navigation bar)', null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='short_name_pt_br',
            field=models.CharField(default=b'Cat1', max_length=40, verbose_name='Category Short Name (for navigation bar)', null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='short_name_ru',
            field=models.CharField(default=b'Cat1', max_length=40, verbose_name='Category Short Name (for navigation bar)', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.CharField(max_length=255, verbose_name='Product Description', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_es',
            field=models.CharField(max_length=255, verbose_name='Product Description', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_pt_br',
            field=models.CharField(max_length=255, verbose_name='Product Description', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.CharField(max_length=255, verbose_name='Product Description', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='long_name_en',
            field=models.CharField(max_length=255, verbose_name='Product Long Name', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='long_name_es',
            field=models.CharField(max_length=255, verbose_name='Product Long Name', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='long_name_pt_br',
            field=models.CharField(max_length=255, verbose_name='Product Long Name', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='long_name_ru',
            field=models.CharField(max_length=255, verbose_name='Product Long Name', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='long_text_en',
            field=ckeditor.fields.RichTextField(verbose_name='Product Long Text', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='long_text_es',
            field=ckeditor.fields.RichTextField(verbose_name='Product Long Text', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='long_text_pt_br',
            field=ckeditor.fields.RichTextField(verbose_name='Product Long Text', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='long_text_ru',
            field=ckeditor.fields.RichTextField(verbose_name='Product Long Text', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(default=b'Product 1', max_length=100, verbose_name='Product Short Name', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_es',
            field=models.CharField(default=b'Product 1', max_length=100, verbose_name='Product Short Name', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_pt_br',
            field=models.CharField(default=b'Product 1', max_length=100, verbose_name='Product Short Name', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(default=b'Product 1', max_length=100, verbose_name='Product Short Name', null=True),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_title_en',
            field=models.CharField(max_length=200, verbose_name='Picture Title', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_title_es',
            field=models.CharField(max_length=200, verbose_name='Picture Title', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_title_pt_br',
            field=models.CharField(max_length=200, verbose_name='Picture Title', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_title_ru',
            field=models.CharField(max_length=200, verbose_name='Picture Title', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shopimage',
            name='image_title_en',
            field=models.CharField(max_length=255, verbose_name='Picture Title', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shopimage',
            name='image_title_es',
            field=models.CharField(max_length=255, verbose_name='Picture Title', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shopimage',
            name='image_title_pt_br',
            field=models.CharField(max_length=255, verbose_name='Picture Title', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shopimage',
            name='image_title_ru',
            field=models.CharField(max_length=255, verbose_name='Picture Title', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description_en',
            field=models.CharField(max_length=255, verbose_name='Subcategory description', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description_es',
            field=models.CharField(max_length=255, verbose_name='Subcategory description', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description_pt_br',
            field=models.CharField(max_length=255, verbose_name='Subcategory description', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description_ru',
            field=models.CharField(max_length=255, verbose_name='Subcategory description', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='long_text_en',
            field=ckeditor.fields.RichTextField(verbose_name='Subcategory Long Text (Please do not insert images!)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='long_text_es',
            field=ckeditor.fields.RichTextField(verbose_name='Subcategory Long Text (Please do not insert images!)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='long_text_pt_br',
            field=ckeditor.fields.RichTextField(verbose_name='Subcategory Long Text (Please do not insert images!)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='long_text_ru',
            field=ckeditor.fields.RichTextField(verbose_name='Subcategory Long Text (Please do not insert images!)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_en',
            field=models.CharField(default=b'Subcategory 1', max_length=255, verbose_name='Subcategory Name', null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_es',
            field=models.CharField(default=b'Subcategory 1', max_length=255, verbose_name='Subcategory Name', null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_pt_br',
            field=models.CharField(default=b'Subcategory 1', max_length=255, verbose_name='Subcategory Name', null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_ru',
            field=models.CharField(default=b'Subcategory 1', max_length=255, verbose_name='Subcategory Name', null=True),
        ),
    ]
