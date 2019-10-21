# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-21 14:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Soundable', '0007_auto_20191021_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song_table',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
