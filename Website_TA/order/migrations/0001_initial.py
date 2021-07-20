# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-20 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pesanan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kebutuhan_mesin', models.CharField(max_length=20)),
                ('kebutuhan_lapak', models.IntegerField(null=True)),
                ('kebutuhan_group', models.IntegerField(null=True)),
                ('waktu_mulai', models.DateTimeField()),
            ],
        ),
    ]
