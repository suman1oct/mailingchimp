# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 22:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chimp', '0014_auto_20170425_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='templatelist',
            old_name='path',
            new_name='file',
        ),
        migrations.RemoveField(
            model_name='mailinglist',
            name='upload_date',
        ),
    ]
