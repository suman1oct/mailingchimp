# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chimp', '0012_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailinglist',
            name='upload_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]