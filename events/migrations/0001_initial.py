# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('importance', models.CharField(default=b'B', max_length=2, choices=[('A', 'Critical Importance'), ('B', 'Medium Importance'), ('C', 'Trivial Importance')])),
                ('date', models.DateField()),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Event Type',
                'verbose_name_plural': 'Event Types',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(to='events.EventType'),
        ),
    ]
