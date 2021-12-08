# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-01 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_newsletterrecipients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='editor',
        ),
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='newsletterrecipients',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Editor',
        ),
    ]
