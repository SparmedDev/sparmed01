# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('online_order', '0012_auto_20150706_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparmeduser',
            name='groups',
            field=models.ManyToManyField(related_name='user_set', related_query_name='user', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', blank=True),
        ),
        migrations.AddField(
            model_name='sparmeduser',
            name='is_superuser',
            field=models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.'),
        ),
        migrations.AddField(
            model_name='sparmeduser',
            name='user_permissions',
            field=models.ManyToManyField(related_name='user_set', related_query_name='user', verbose_name='user permissions', help_text='Specific permissions for this user.', to='auth.Permission', blank=True),
        ),
    ]
