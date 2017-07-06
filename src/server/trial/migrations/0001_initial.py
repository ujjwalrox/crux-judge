# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-04 21:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('problem_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('statement', models.CharField(max_length=1000)),
                ('output', models.CharField(max_length=100)),
                ('uploadedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='problem-setter')),
            ],
            options={
                'verbose_name': 'problem',
                'ordering': ['problem_id'],
            },
        ),
    ]