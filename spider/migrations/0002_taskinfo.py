# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='taskinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dramaurl', models.TextField(max_length=1000, null=True, verbose_name=b'\xe7\x88\xac\xe5\x8f\x96\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('episode', models.CharField(max_length=50, null=True, verbose_name=b'\xe9\x9b\x86\xe6\x95\xb0', blank=True)),
                ('downloadurl', models.TextField(max_length=1000, null=True, verbose_name=b'\xe4\xb8\x8b\xe8\xbd\xbd\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('linkmd5id', models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x94\xaf\xe4\xb8\x80ID', blank=True)),
                ('downloadstatus', models.CharField(max_length=5, null=True, verbose_name=b'\xe4\xb8\x8b\xe8\xbd\xbd\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
                ('stime', models.DateTimeField(default=b'2016-01-01 00:00:00', verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe6\x8a\x93\xe5\x8f\x96\xe6\x97\xb6\xe9\x97\xb4')),
                ('etime', models.DateTimeField(default=b'2016-01-01 00:00:00', verbose_name=b'\xe4\xb8\x8b\xe8\xbd\xbd\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
    ]
