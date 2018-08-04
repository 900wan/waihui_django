# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-07 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_auto_20180306_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModelformFK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Provider')),
            ],
            options={
                'verbose_name': 'TestModelformFK',
                'verbose_name_plural': 'TestModelformFKs',
            },
        ),
    ]