# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 08:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chimp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='businees_name',
            new_name='business_name',
        ),
    ]
