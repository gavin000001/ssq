# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-02 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myssq', '0004_doubleball'),
    ]

    operations = [
        migrations.AddField(
            model_name='doubleball',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
