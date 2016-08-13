# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luzhi', '0003_channel_task_taskid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel_task',
            name='channelid',
            field=models.CharField(max_length=255, verbose_name=b'\xe9\xa2\x91\xe9\x81\x93ID'),
        ),
    ]
