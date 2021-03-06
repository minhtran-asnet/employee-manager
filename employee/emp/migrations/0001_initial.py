# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-11-03 02:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('status', models.SmallIntegerField(choices=[(0, 'inactive'), (1, 'active')])),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Department')),
            ],
        ),
    ]
