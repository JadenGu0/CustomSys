#coding=utf-8
from django.db import models
from custom.models import Custom, Lot


# Create your models here.

class Commission(models.Model):
    owner = models.ForeignKey(Custom, related_name='who',verbose_name="客户")
    mount = models.FloatField(verbose_name="金额")
