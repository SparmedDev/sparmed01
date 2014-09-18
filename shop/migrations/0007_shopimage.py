# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20140911_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopImage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('image_title', models.CharField(blank=True, verbose_name=b'Picture Title', max_length=255)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=b'/media/products')),
                ('category', models.ForeignKey(related_name=b'images', to='shop.Subcategory', verbose_name=b'Associated Subcategory', blank=True, null=True)),
                ('subcategory', models.ForeignKey(related_name=b'images', to='shop.Category', verbose_name=b'Associated Category', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
