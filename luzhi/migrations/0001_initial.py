# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channelid', models.CharField(unique=True, max_length=255, verbose_name=b'\xe9\xa2\x91\xe9\x81\x93ID')),
                ('channelname', models.CharField(max_length=255, null=True, verbose_name=b'\xe9\xa2\x91\xe9\x81\x93\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('channelurl', models.CharField(max_length=255, null=True, verbose_name=b'\xe6\xba\x90\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='channel_task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('taskname', models.CharField(max_length=255, null=True, verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('stime', models.DateTimeField(verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('etime', models.DateTimeField(verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4')),
                ('taskstatus', models.CharField(default=b'1', max_length=5, verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe7\x8a\xb6\xe6\x80\x81')),
                ('channelid', models.ForeignKey(related_name='recode_task', to='luzhi.channel')),
            ],
        ),
    ]
