# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 14:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chimp', '0021_auto_20170501_1348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailinglist',
            old_name='file',
            new_name='mailing_list_path',
        ),
    ]
