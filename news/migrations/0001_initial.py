# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(verbose_name=b'Picture Title', blank=True, max_length=200)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=b'/media/news')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('added', models.DateTimeField(verbose_name=b'Date and time added', default=datetime.datetime.now)),
                ('content', models.TextField(verbose_name=b'Write your news post here (Please do not attempt to insert images here, instead use the news image below)')),
                ('slug', models.SlugField(verbose_name=b'URL; Never modify this value!', max_length=255, unique=True)),
            ],
            options={
                'ordering': ['-added'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='newsimage',
            name='news_post',
            field=models.ForeignKey(related_name=b'images', verbose_name=b'Associated News Post', to='news.NewsPost'),
            preserve_default=True,
        ),
    ]
