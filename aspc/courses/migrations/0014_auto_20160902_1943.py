# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-02 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20160902_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericsection',
            name='approachable_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genericsection',
            name='competency_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genericsection',
            name='difficulty_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genericsection',
            name='engagement_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genericsection',
            name='enthusiasm_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genericsection',
            name='lecturing_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genericsection',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genericsection',
            name='useful_rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
