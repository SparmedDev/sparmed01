# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificateitem',
            name='group',
            field=models.ForeignKey(related_name=b'items', to='certificates.CertificateGroup'),
        ),
        migrations.AlterField(
            model_name='certificateitem',
            name='subgroup',
            field=models.ForeignKey(related_name=b'items', to='certificates.CertificateSubgroup'),
        ),
    ]
