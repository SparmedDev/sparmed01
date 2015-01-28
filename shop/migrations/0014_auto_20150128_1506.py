# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import validatedfile.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20141016_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='document',
            field=validatedfile.fields.ValidatedFileField(verbose_name=b'PDF Document file (56 MB max)', blank=True, null=True, upload_to=b'/documents/'),
        ),
    ]
