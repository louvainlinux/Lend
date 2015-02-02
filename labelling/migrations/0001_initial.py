# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('notes', models.TextField(default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(to='labelling.EquipmentType', related_name='children', blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('notes', models.TextField(default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('contained_by', models.ForeignKey(to='labelling.Label', blank=True, null=True, default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LabelType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(to='labelling.LabelType', related_name='children', blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='label',
            name='type',
            field=models.ForeignKey(to='labelling.LabelType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipment',
            name='location',
            field=models.ForeignKey(to='labelling.Label'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipment',
            name='type',
            field=models.ForeignKey(to='labelling.EquipmentType'),
            preserve_default=True,
        ),
    ]
