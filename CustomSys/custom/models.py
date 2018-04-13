#coding=utf-8
from django.db import models

import datetime


# Create your models here.



class Custom(models.Model):
    TYPT_CHOICE = (
        (1, 'custom'),
        (2, 'ib'),
        (3, 'mib'),
        (4, 'pib'),
    )
    name = models.CharField(max_length=255,verbose_name="用户名")
    account = models.IntegerField(blank=True, null=True,verbose_name="账号")
    init_money = models.FloatField(blank=True,verbose_name="初始入金")
    create_time = models.DateField(blank=True,verbose_name="开户时间")
    commission = models.IntegerField(verbose_name="佣金")
    type = models.IntegerField(choices=TYPT_CHOICE, default=1,verbose_name="类型")
    upper = models.ForeignKey('self', related_name="upper_class", blank=True, null=True,verbose_name="直属上级")

    def __str__(self):
        return self.name + '-' + self.get_type_display()

class Lot(models.Model):
    start_time = models.DateField(verbose_name="开始时间")
    end_time = models.DateField(verbose_name="结束时间")
    lot = models.FloatField(verbose_name="手数")
    custom=models.ForeignKey(Custom,related_name="lot_set",null=True,verbose_name="客户")

    def __str__(self):
        return self.start_time.strftime ('%Y-%m') + '-' + self.custom.name+'-'+str(self.lot)

