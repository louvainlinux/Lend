# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labelling', '0004_auto_20141127_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lending',
            name='end',
            field=models.DateField(blank=True, default=None, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lending',
            name='start',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
