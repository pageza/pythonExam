# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 22:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170225_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('quote', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='main.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='like',
            name='liked',
        ),
        migrations.RemoveField(
            model_name='like',
            name='liker',
        ),
        migrations.RemoveField(
            model_name='secret',
            name='user',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Secret',
        ),
    ]
