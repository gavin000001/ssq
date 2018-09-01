# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class DoubleBallAll(models.Model):
    red1 = models.IntegerField()
    red2 = models.IntegerField()
    red3 = models.IntegerField()
    red4 = models.IntegerField()
    red5 = models.IntegerField()
    red6 = models.IntegerField()
    blue = models.IntegerField()
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.blue
    class Meta:
        verbose_name = '全部数据'
        db_table = 'doubleball_all'
        verbose_name_plural = verbose_name

class DoubleBall(models.Model):
    qici = models.CharField(max_length=20)
    date = models.DateField(blank=True, null=True)
    red1 = models.IntegerField()
    red2 = models.IntegerField()
    red3 = models.IntegerField()
    red4 = models.IntegerField()
    red5 = models.IntegerField()
    red6 = models.IntegerField()
    blue = models.IntegerField()

    def __str__(self):
        return self.qici
    class Meta:
        verbose_name = '历史数据'
        db_table = 'doubleball'
        verbose_name_plural = verbose_name
