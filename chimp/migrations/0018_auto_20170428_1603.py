# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-28 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chimp', '0017_auto_20170428_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='templatelist',
            old_name='path',
            new_name='file',
        ),
        migrations.AlterField(
            model_name='mailinglist',
            name='mailing_list_path',
            field=models.FileField(upload_to='uploads/excels/'),
        ),
    ]
