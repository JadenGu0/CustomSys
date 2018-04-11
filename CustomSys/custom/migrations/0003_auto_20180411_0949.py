# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0002_auto_20180411_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('lot', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='custom',
            name='account',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='custom',
            name='lot',
            field=models.ManyToManyField(to='custom.Lot'),
        ),
    ]
