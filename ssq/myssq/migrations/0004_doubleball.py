# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-02 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myssq', '0003_auto_20180602_0308'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoubleBall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qici', models.CharField(max_length=20)),
                ('red1', models.IntegerField()),
                ('red2', models.IntegerField()),
                ('red3', models.IntegerField()),
                ('red4', models.IntegerField()),
                ('red5', models.IntegerField()),
                ('red6', models.IntegerField()),
                ('blue', models.IntegerField()),
            ],
            options={
                'db_table': 'doubleball',
                'verbose_name': '\u5386\u53f2\u6570\u636e',
                'verbose_name_plural': '\u5386\u53f2\u6570\u636e',
            },
        ),
    ]
