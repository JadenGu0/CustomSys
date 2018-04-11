# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Custom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('init_money', models.FloatField(blank=True)),
                ('create_time', models.DateField(blank=True)),
                ('commission', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MIB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PIB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='custom',
            name='ib',
            field=models.ForeignKey(to='custom.IB', blank=True),
        ),
        migrations.AddField(
            model_name='custom',
            name='mib',
            field=models.ForeignKey(to='custom.MIB', blank=True),
        ),
        migrations.AddField(
            model_name='custom',
            name='pib',
            field=models.ForeignKey(to='custom.PIB', blank=True),
        ),
    ]
