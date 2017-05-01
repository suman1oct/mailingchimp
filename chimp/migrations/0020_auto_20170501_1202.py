# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chimp', '0019_auto_20170429_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='mailing_list_path',
            field=models.FileField(upload_to='excels/'),
        ),
        migrations.AlterField(
            model_name='templatelist',
            name='file',
            field=models.FileField(upload_to='templates/'),
        ),
        migrations.AlterField(
            model_name='templatelist',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
