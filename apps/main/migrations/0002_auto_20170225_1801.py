# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 00:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='liked',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked', to='main.Secret'),
        ),
    ]
