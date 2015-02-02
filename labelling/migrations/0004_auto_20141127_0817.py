# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('labelling', '0003_auto_20141127_0745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=75)),
                ('address', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BorrowerType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', null=True, blank=True, to='labelling.BorrowerType')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lending',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField(default=None, blank=True, null=True)),
                ('deposit', models.DecimalField(default=50, decimal_places=2, max_digits=6)),
                ('price', models.DecimalField(default=0, decimal_places=2, max_digits=6)),
                ('complete', models.BooleanField(default=False)),
                ('deposit_kept', models.DecimalField(default=None, decimal_places=2, max_digits=6, blank=True, null=True)),
                ('borrower', models.ForeignKey(to='labelling.Borrower')),
                ('label', models.ForeignKey(to='labelling.Label')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='borrower',
            name='type',
            field=mptt.fields.TreeForeignKey(to='labelling.BorrowerType'),
            preserve_default=True,
        ),
    ]
