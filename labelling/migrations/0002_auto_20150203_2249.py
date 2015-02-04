# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labelling', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lending',
            name='label',
        ),
        migrations.AddField(
            model_name='equipment',
            name='borrowed',
            field=models.ForeignKey(blank=True, null=True, default=None, to='labelling.Lending', related_name='borrowed_equipments'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='label',
            name='borrowed',
            field=models.ForeignKey(blank=True, null=True, default=None, to='labelling.Lending', related_name='borrowed_labels'),
            preserve_default=True,
        ),
    ]
