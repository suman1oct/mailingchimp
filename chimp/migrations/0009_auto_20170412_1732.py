# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chimp', '0008_auto_20170412_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatelist',
            name='category',
            field=models.CharField(choices=[('PM', 'promotional'), ('AD', 'advertisement'), ('SL', 'social'), ('OT', 'others')], default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
