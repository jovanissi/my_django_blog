# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20170223_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='headlines',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='headlines',
            name='classifications',
            field=models.CharField(choices=[('Tech', 'Tech'), ('Science', 'Science'), ('Social', 'Social')], default='Tech', max_length=200),
        ),
    ]
