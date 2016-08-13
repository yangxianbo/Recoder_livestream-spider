# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luzhi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='offset',
            field=models.CharField(default=b'0', max_length=5, verbose_name=b'\xe5\x81\x8f\xe7\xa7\xbb\xe9\x87\x8f'),
        ),
    ]
