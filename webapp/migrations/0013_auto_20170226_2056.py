# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_auto_20170226_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='webapp.headlines'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='headlines',
            name='classifications',
            field=models.CharField(choices=[('Tech', 'Tech'), ('Social', 'Social'), ('Science', 'Science')], default='Tech', max_length=200),
        ),
    ]