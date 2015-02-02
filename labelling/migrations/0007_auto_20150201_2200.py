# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labelling', '0006_config'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='id',
        ),
        migrations.AlterField(
            model_name='config',
            name='name',
            field=models.TextField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
