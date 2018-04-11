from django.db import models
from custom.models import Custom, Lot


# Create your models here.

class Commission(models.Model):
    owner = models.ForeignKey(Custom, related_name='who')
    mount = models.FloatField()
