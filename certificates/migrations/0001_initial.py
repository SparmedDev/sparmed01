# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import validatedfile.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateGroup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name=b'Group Title/Name')),
                ('order_index', models.PositiveIntegerField(null=True, default=0, blank=True)),
                ('added', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Date and time added')),
            ],
            options={
                'ordering': ['order_index', 'added'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CertificateItem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name=b'Certificate/Document Title')),
                ('document', validatedfile.fields.ValidatedFileField(null=True, upload_to=b'/certificates/', blank=True, verbose_name=b'PDF Document file (256 MB max)')),
                ('order_index', models.PositiveIntegerField(null=True, default=0, blank=True)),
                ('added', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Date and time added')),
                ('group', models.ForeignKey(related_name=b'products', to='certificates.CertificateGroup')),
            ],
            options={
                'ordering': ['order_index', 'added'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CertificateSubgroup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name=b'Subgroup Title/Name')),
                ('order_index', models.PositiveIntegerField(null=True, default=0, blank=True)),
                ('added', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Date and time added')),
                ('group', models.ForeignKey(related_name=b'subgroups', to='certificates.CertificateGroup', verbose_name=b'Associated Group')),
            ],
            options={
                'ordering': ['order_index', 'added'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='certificateitem',
            name='subgroup',
            field=models.ForeignKey(related_name=b'products', to='certificates.CertificateSubgroup'),
            preserve_default=True,
        ),
    ]
