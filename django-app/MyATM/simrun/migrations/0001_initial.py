# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SimRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=10, verbose_name='周期', choices=[('m1', '一分钟'), ('d1', '一天')])),
                ('bgnDttm', models.DateTimeField(verbose_name='开始时间')),
                ('endDttm', models.DateTimeField(verbose_name='结束时间')),
                ('runDttm', models.DateTimeField(verbose_name='运行时间')),
            ],
            options={
                'verbose_name_plural': '模拟运行',
                'verbose_name': '模拟运行',
            },
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
            ],
            options={
                'verbose_name_plural': '策略（Strategy）',
                'verbose_name': '策略（Strategy）',
            },
        ),
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
            ],
            options={
                'verbose_name_plural': '商品（Symbol）',
                'verbose_name': '商品（Symbol）',
            },
        ),
        migrations.AddField(
            model_name='simrun',
            name='strategy',
            field=models.ForeignKey(verbose_name='策略', to='simrun.Strategy'),
        ),
        migrations.AddField(
            model_name='simrun',
            name='symbol',
            field=models.ForeignKey(verbose_name='商品', to='simrun.Symbol'),
        ),
    ]
