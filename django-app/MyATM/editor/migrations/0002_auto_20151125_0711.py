# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='script',
            options={'verbose_name': '脚本', 'verbose_name_plural': '脚本'},
        ),
    ]
