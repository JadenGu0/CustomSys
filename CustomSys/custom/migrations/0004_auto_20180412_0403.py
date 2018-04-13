# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0003_auto_20180411_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom',
            name='lot',
        ),
        migrations.AddField(
            model_name='lot',
            name='custom',
            field=models.ForeignKey(related_name='who_lot', to='custom.Custom', null=True),
        ),
    ]
