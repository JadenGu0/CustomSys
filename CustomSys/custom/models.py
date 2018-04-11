from django.db import models
import datetime


# Create your models here.
class Lot(models.Model):
    start_time = models.DateField()
    end_time = models.DateField()
    lot = models.FloatField()

    def __str__(self):
        return self.start_time.strftime('%Y-%m-%d') + '-' + self.end_time.strftime('%Y-%m-%d')


class Custom(models.Model):
    TYPT_CHOICE = (
        (1, 'custom'),
        (2, 'ib'),
        (3, 'mib'),
        (4, 'pib'),
    )
    name = models.CharField(max_length=255)
    account = models.IntegerField(blank=True, null=True)
    init_money = models.FloatField(blank=True)
    create_time = models.DateField(blank=True)
    commission = models.IntegerField()
    type = models.IntegerField(choices=TYPT_CHOICE, default=1)
    upper = models.ForeignKey('self', related_name="upper_class", blank=True, null=True)
    lot = models.ManyToManyField(Lot)

    def __str__(self):
        return self.name + '-' + self.get_type_display()
