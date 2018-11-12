# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-12 05:57
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Practice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='player',
            name='match',
        ),
        migrations.RemoveField(
            model_name='player',
            name='partner_choice',
        ),
        migrations.RemoveField(
            model_name='player',
            name='signal',
        ),
        migrations.RemoveField(
            model_name='subsession',
            name='game',
        ),
        migrations.RemoveField(
            model_name='subsession',
            name='game_name',
        ),
        migrations.AddField(
            model_name='player',
            name='bid',
            field=otree.db.models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='rank',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='side',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='partner_type',
            field=otree.db.models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='points',
            field=otree.db.models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='type',
            field=otree.db.models.FloatField(null=True),
        ),
    ]
