# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('labelling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='location',
            field=mptt.fields.TreeForeignKey(to='labelling.Label'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='label',
            name='type',
            field=mptt.fields.TreeForeignKey(to='labelling.LabelType'),
            preserve_default=True,
        ),
    ]
