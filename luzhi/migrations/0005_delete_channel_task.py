# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luzhi', '0004_auto_20160621_1841'),
    ]

    operations = [
        migrations.DeleteModel(
            name='channel_task',
        ),
    ]
