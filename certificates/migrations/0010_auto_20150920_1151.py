# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import validatedfile.fields


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0009_auto_20150707_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificateitem',
            name='document',
            field=validatedfile.fields.ValidatedFileField(verbose_name='PDF Document file (256 MB max)', blank=True, null=True, upload_to=b'certificates/'),
        ),
    ]
