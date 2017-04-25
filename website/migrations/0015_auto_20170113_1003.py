# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-13 08:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20170112_1040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['first', 'last'], 'verbose_name_plural': 'people'},
        ),
        migrations.RemoveField(
            model_name='species',
            name='assessor',
        ),
        migrations.RemoveField(
            model_name='species',
            name='reviewer',
        ),
    ]