# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-01 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algorithms', '0003_auto_20170429_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='result',
            field=models.FileField(upload_to=''),
        ),
    ]