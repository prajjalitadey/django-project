# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_latest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='tmdb_id',
            field=models.IntegerField(null=True),
        ),
    ]
