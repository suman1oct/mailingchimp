# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 05:32
from __future__ import unicode_literals

import chimp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chimp', '0024_auto_20170503_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='mailing_list_path',
            field=models.FileField(upload_to=chimp.models.get_file_path),
        ),
    ]
