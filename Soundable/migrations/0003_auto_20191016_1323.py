# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-16 13:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Soundable', '0002_auto_20191004_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_address', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('date_of_purchase', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='purchases',
            name='purchased_by',
        ),
        migrations.RemoveField(
            model_name='purchases',
            name='song',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_employee',
        ),
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='purchases',
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchased_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchase',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Soundable.song_table'),
        ),
    ]
