# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20170222_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='headlines',
            name='number_view',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='headlines',
            name='classifications',
            field=models.CharField(choices=[('Science', 'Science'), ('Tech', 'Tech'), ('Social', 'Social')], default='Tech', max_length=200),
        ),
    ]
