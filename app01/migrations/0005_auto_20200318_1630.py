# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-18 08:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20200318_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='uesr',
            new_name='user',
        ),
    ]
