# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-08-26 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='sex',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='password',
            field=models.CharField(default=1, max_length=18),
            preserve_default=False,
        ),
    ]
