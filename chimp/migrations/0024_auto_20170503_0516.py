# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chimp', '0023_auto_20170503_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]