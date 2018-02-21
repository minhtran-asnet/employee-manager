# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-11-03 02:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp.Employee')),
            ],
        ),
    ]
