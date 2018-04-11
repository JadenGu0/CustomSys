# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0003_auto_20180411_0949'),
        ('commission', '0002_auto_20180411_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mount', models.FloatField()),
                ('owner', models.ForeignKey(related_name='who', to='custom.Custom')),
            ],
        ),
    ]
