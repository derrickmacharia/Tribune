# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-01 20:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20211201_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='editor',
        ),
        migrations.DeleteModel(
            name='Editor',
        ),
    ]
