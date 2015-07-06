# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Category description'),
        ),
        migrations.AddField(
            model_name='category',
            name='description_es',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Category description'),
        ),
        migrations.AddField(
            model_name='category',
            name='description_pt_br',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Category description'),
        ),
        migrations.AddField(
            model_name='category',
            name='description_ru',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Category description'),
        ),
        migrations.AddField(
            model_name='category',
            name='long_text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Category Long Text (Please do not insert images!)'),
        ),
        migrations.AddField(
            model_name='category',
            name='long_text_es',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Category Long Text (Please do not insert images!)'),
        ),
        migrations.AddField(
            model_name='category',
            name='long_text_pt_br',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Category Long Text (Please do not insert images!)'),
        ),
        migrations.AddField(
            model_name='category',
            name='long_text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Category Long Text (Please do not insert images!)'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(default=b'Category 1', null=True, max_length=255, verbose_name='Category Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_es',
            field=models.CharField(default=b'Category 1', null=True, max_length=255, verbose_name='Category Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_pt_br',
            field=models.CharField(default=b'Category 1', null=True, max_length=255, verbose_name='Category Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(default=b'Category 1', null=True, max_length=255, verbose_name='Category Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='short_name_en',
            field=models.CharField(default=b'Cat1', null=True, max_length=40, verbose_name='Category Short Name (for navigation bar)'),
        ),
        migrations.AddField(
            model_name='category',
            name='short_name_es',
            field=models.CharField(default=b'Cat1', null=True, max_length=40, verbose_name='Category Short Name (for navigation bar)'),
        ),
        migrations.AddField(
            model_name='category',
            name='short_name_pt_br',
            field=models.CharField(default=b'Cat1', null=True, max_length=40, verbose_name='Category Short Name (for navigation bar)'),
        ),
        migrations.AddField(
            model_name='category',
            name='short_name_ru',
            field=models.CharField(default=b'Cat1', null=True, max_length=40, verbose_name='Category Short Name (for navigation bar)'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Product Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_es',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Product Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_pt_br',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Product Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Product Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='long_name_en',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Product Long Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='long_name_es',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Product Long Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='long_name_pt_br',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Product Long Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='long_name_ru',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Product Long Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='long_text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Product Long Text'),
        ),
        migrations.AddField(
            model_name='product',
            name='long_text_es',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Product Long Text'),
        ),
        migrations.AddField(
            model_name='product',
            name='long_text_pt_br',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Product Long Text'),
        ),
        migrations.AddField(
            model_name='product',
            name='long_text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Product Long Text'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(default=b'Product 1', null=True, max_length=100, verbose_name='Product Short Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_es',
            field=models.CharField(default=b'Product 1', null=True, max_length=100, verbose_name='Product Short Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_pt_br',
            field=models.CharField(default=b'Product 1', null=True, max_length=100, verbose_name='Product Short Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(default=b'Product 1', null=True, max_length=100, verbose_name='Product Short Name'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_title_en',
            field=models.CharField(null=True, blank=True, max_length=200, verbose_name='Picture Title'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_title_es',
            field=models.CharField(null=True, blank=True, max_length=200, verbose_name='Picture Title'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_title_pt_br',
            field=models.CharField(null=True, blank=True, max_length=200, verbose_name='Picture Title'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_title_ru',
            field=models.CharField(null=True, blank=True, max_length=200, verbose_name='Picture Title'),
        ),
        migrations.AddField(
            model_name='shopimage',
            name='image_title_en',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Picture Title'),
        ),
        migrations.AddField(
            model_name='shopimage',
            name='image_title_es',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Picture Title'),
        ),
        migrations.AddField(
            model_name='shopimage',
            name='image_title_pt_br',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Picture Title'),
        ),
        migrations.AddField(
            model_name='shopimage',
            name='image_title_ru',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Picture Title'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description_en',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Subcategory description'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description_es',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Subcategory description'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description_pt_br',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Subcategory description'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description_ru',
            field=models.CharField(null=True, blank=True, max_length=255, verbose_name='Subcategory description'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='long_text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Subcategory Long Text (Please do not insert images!)'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='long_text_es',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Subcategory Long Text (Please do not insert images!)'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='long_text_pt_br',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Subcategory Long Text (Please do not insert images!)'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='long_text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Subcategory Long Text (Please do not insert images!)'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_en',
            field=models.CharField(default=b'Subcategory 1', null=True, max_length=255, verbose_name='Subcategory Name'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_es',
            field=models.CharField(default=b'Subcategory 1', null=True, max_length=255, verbose_name='Subcategory Name'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_pt_br',
            field=models.CharField(default=b'Subcategory 1', null=True, max_length=255, verbose_name='Subcategory Name'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_ru',
            field=models.CharField(default=b'Subcategory 1', null=True, max_length=255, verbose_name='Subcategory Name'),
        ),
    ]
