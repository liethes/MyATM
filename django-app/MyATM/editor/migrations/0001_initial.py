# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='脚本名', max_length=100)),
                ('title', models.CharField(verbose_name='标题', max_length=100)),
                ('desc', models.TextField(verbose_name='描述')),
                ('code', models.TextField(verbose_name='代码')),
                ('run_engine', models.CharField(verbose_name='运行引擎', choices=[('MC', 'MultiCharts'), ('TB', 'TradeBlazer')], max_length=5)),
                ('source', models.CharField(verbose_name='来源', max_length=100)),
                ('create_date', models.DateField(verbose_name='创建日期')),
                ('modify_date', models.DateField(verbose_name='修改日期')),
            ],
        ),
    ]
