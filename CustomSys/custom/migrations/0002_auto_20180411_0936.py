# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom',
            name='ib',
        ),
        migrations.RemoveField(
            model_name='custom',
            name='mib',
        ),
        migrations.RemoveField(
            model_name='custom',
            name='pib',
        ),
        migrations.AddField(
            model_name='custom',
            name='type',
            field=models.IntegerField(default=1, choices=[(1, b'custom'), (2, b'ib'), (3, b'mib'), (4, b'pib')]),
        ),
        migrations.AddField(
            model_name='custom',
            name='upper',
            field=models.ForeignKey(related_name='upper_class', blank=True, to='custom.Custom', null=True),
        ),
        migrations.DeleteModel(
            name='IB',
        ),
        migrations.DeleteModel(
            name='MIB',
        ),
        migrations.DeleteModel(
            name='PIB',
        ),
    ]
