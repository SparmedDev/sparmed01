# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import validatedfile.fields
import datetime
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name=b'Category Name', default=b'Category 1', max_length=255)),
                ('short_name', models.CharField(verbose_name=b'Category Short Name (for navigation bar)', default=b'Cat1', max_length=20)),
                ('description', models.CharField(verbose_name=b'Category description', blank=True, max_length=255)),
                ('long_text', models.TextField(verbose_name=b'Category Long Text (Please do not insert images!)', blank=True)),
                ('added', models.DateTimeField(verbose_name=b'Date and time added', default=datetime.datetime.now)),
                ('slug', models.SlugField(verbose_name=b'URL; Never modify this value!', max_length=255, unique=True)),
                ('document', validatedfile.fields.ValidatedFileField(verbose_name=b'PDF Document file (256 MB max)', blank=True, null=True, upload_to=b'/documents/')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['-added'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(verbose_name=b'Product ID', default=b'OOOO-0000', max_length=255)),
                ('name', models.CharField(verbose_name=b'Product Name', default=b'Product 1', max_length=255)),
                ('in_stock', models.IntegerField(verbose_name=b'Amount on Stock', default=0)),
                ('description', models.CharField(verbose_name=b'Product description', blank=True, max_length=255)),
                ('added', models.DateTimeField(verbose_name=b'Date and time added', default=datetime.datetime.now)),
                ('slug', models.SlugField(verbose_name=b'URL; Never modify this value!', max_length=255, unique=True)),
                ('category', models.ForeignKey(related_name=b'products', verbose_name=b'Associated Category', to='shop.Category')),
            ],
            options={
                'ordering': ['-added'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(verbose_name=b'Picture Title', blank=True, max_length=200)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=b'/media/products')),
                ('product', models.ForeignKey(related_name=b'images', verbose_name=b'Associated Product', to='shop.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name=b'Subcategory Name', default=b'Subcategory 1', max_length=255)),
                ('description', models.CharField(verbose_name=b'Subcategory description', blank=True, max_length=255)),
                ('long_text', models.TextField(verbose_name=b'Subcategory Long Text (Please do not insert images!)', blank=True)),
                ('added', models.DateTimeField(verbose_name=b'Date and time added', default=datetime.datetime.now)),
                ('slug', models.SlugField(verbose_name=b'URL; Never modify this value!', max_length=255, unique=True)),
                ('category', models.ForeignKey(related_name=b'subcategories', verbose_name=b'Associated Category', to='shop.Category')),
            ],
            options={
                'verbose_name_plural': 'Subcategories',
                'ordering': ['-added'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(related_name=b'products', verbose_name=b'Associated Subcategory', to='shop.Subcategory'),
            preserve_default=True,
        ),
    ]
