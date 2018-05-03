# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-11 09:27
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cursedsearch', '0011_auto_20180311_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='pair',
        ),
        migrations.AddField(
            model_name='player',
            name='partner',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]