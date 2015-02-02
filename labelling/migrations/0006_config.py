# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labelling', '0005_auto_20141127_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.TextField()),
                ('value', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
