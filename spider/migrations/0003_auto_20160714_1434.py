# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0002_taskinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinfo',
            name='etime',
            field=models.DateTimeField(null=True, verbose_name=b'\xe4\xb8\x8b\xe8\xbd\xbd\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
        migrations.AlterField(
            model_name='taskinfo',
            name='stime',
            field=models.DateTimeField(null=True, verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe6\x8a\x93\xe5\x8f\x96\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
    ]
