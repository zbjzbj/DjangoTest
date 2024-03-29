# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-08-19 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=20)),
                ('sex', models.IntegerField(choices=[(1, '男'), (2, '女'), (3, '保密')], default=3)),
                ('bool_field', models.BooleanField()),
                ('text_field', models.TextField()),
                ('email_field', models.EmailField(max_length=254)),
                ('ip_field', models.GenericIPAddressField()),
                ('uuid_field', models.UUIDField()),
                ('image_field', models.ImageField(upload_to='image/%Y-%m')),
                ('datetime_field', models.DateTimeField(auto_now_add=True)),
                ('date_field', models.DateField(auto_now=True)),
                ('time_field', models.TimeField()),
                ('float_field', models.FloatField()),
                ('decimal_Field', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
            options={
                'db_table': 'test',
            },
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=12)),
                ('birthday', models.DateTimeField(auto_now_add=True, null=True, verbose_name='生日')),
                ('sex', models.IntegerField(choices=[(1, '男'), (2, '女'), (3, '保密')], default=3)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='test',
            unique_together=set([('tag', 'sex')]),
        ),
        migrations.AlterIndexTogether(
            name='test',
            index_together=set([('ip_field', 'uuid_field')]),
        ),
    ]
