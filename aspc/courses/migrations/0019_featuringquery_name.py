# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-16 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_auto_20161016_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuringquery',
            name='name',
            field=models.TextField(default='a', max_length=20),
            preserve_default=False,
        ),
    ]
