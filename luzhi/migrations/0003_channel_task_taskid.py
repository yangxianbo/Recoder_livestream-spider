# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luzhi', '0002_channel_offset'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel_task',
            name='taskid',
            field=models.CharField(default=b'1', max_length=5, verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe8\xbf\x9b\xe7\xa8\x8bID'),
        ),
    ]
