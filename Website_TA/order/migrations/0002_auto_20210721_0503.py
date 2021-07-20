# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-20 22:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlatLas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availabilitas', models.BooleanField()),
                ('timeline_alat', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CatElektroplating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availabilitas', models.BooleanField()),
                ('timeline_alat', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupKerja01',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availabilitas', models.BooleanField()),
                ('timeline_group01', models.DateTimeField()),
                ('AlatLas_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.AlatLas')),
                ('CatElektroplating_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.CatElektroplating')),
            ],
        ),
        migrations.CreateModel(
            name='GroupKerja02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availabilitas', models.BooleanField()),
                ('timeline_group02', models.DateTimeField()),
                ('AlatLas_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.AlatLas')),
                ('CatElektroplating_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.CatElektroplating')),
            ],
        ),
        migrations.CreateModel(
            name='KerjaBangku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availabilitas', models.BooleanField()),
                ('timeline_alat', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='KoordinatorGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_available', models.CharField(max_length=20)),
                ('timeline_kosong', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LapakSelatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeline_lapak', models.DateTimeField()),
                ('timeline_group01', models.DateTimeField()),
                ('timeline_group02', models.DateTimeField()),
                ('timeline_group03', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LapakUtara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeline_lapak', models.DateTimeField()),
                ('timeline_group01', models.DateTimeField()),
                ('timeline_group02', models.DateTimeField()),
                ('timeline_group03', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MesinCNC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availabilitas', models.BooleanField()),
                ('timeline_alat', models.DateTimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='pesanan',
            old_name='kebutuhan_mesin',
            new_name='kebutuhan_alat',
        ),
        migrations.AddField(
            model_name='groupkerja02',
            name='KerjaBangku_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.KerjaBangku'),
        ),
        migrations.AddField(
            model_name='groupkerja02',
            name='LapakSelatan_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.LapakSelatan'),
        ),
        migrations.AddField(
            model_name='groupkerja02',
            name='LapakUtara_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.LapakUtara'),
        ),
        migrations.AddField(
            model_name='groupkerja02',
            name='MesinCNC_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.MesinCNC'),
        ),
        migrations.AddField(
            model_name='groupkerja01',
            name='KerjaBangku_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.KerjaBangku'),
        ),
        migrations.AddField(
            model_name='groupkerja01',
            name='LapakSelatan_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.LapakSelatan'),
        ),
        migrations.AddField(
            model_name='groupkerja01',
            name='LapakUtara_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.LapakUtara'),
        ),
        migrations.AddField(
            model_name='groupkerja01',
            name='MesinCNC_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.MesinCNC'),
        ),
    ]