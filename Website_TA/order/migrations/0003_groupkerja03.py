# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-20 22:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210721_0503'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupKerja03',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availabilitas', models.BooleanField()),
                ('timeline_group03', models.DateTimeField()),
                ('AlatLas_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.AlatLas')),
                ('CatElektroplating_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.CatElektroplating')),
                ('KerjaBangku_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.KerjaBangku')),
                ('LapakSelatan_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.LapakSelatan')),
                ('LapakUtara_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.LapakUtara')),
                ('MesinCNC_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.MesinCNC')),
            ],
        ),
    ]
