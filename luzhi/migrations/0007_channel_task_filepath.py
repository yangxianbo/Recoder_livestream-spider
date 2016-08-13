# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('luzhi', '0006_channel_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel_task',
            name='filepath',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe8\xa7\x86\xe9\xa2\x91\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
        ),
    ]
