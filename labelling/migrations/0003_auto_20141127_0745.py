# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('labelling', '0002_auto_20141127_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='location',
            field=models.ForeignKey(to='labelling.Label'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='equipment',
            name='type',
            field=mptt.fields.TreeForeignKey(to='labelling.EquipmentType'),
            preserve_default=True,
        ),
    ]
