# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20170116_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='title',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]