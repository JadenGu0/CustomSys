# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('custom', models.ForeignKey(related_name='which_custom', to='custom.Custom')),
            ],
        ),
    ]
