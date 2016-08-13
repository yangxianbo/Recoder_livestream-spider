# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='taskmain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dirpath', models.CharField(unique=True, max_length=255, verbose_name=b'\xe7\x9b\xae\xe5\xbd\x95\xe4\xbb\xa5\xe5\x8f\x8a\xe4\xb8\x8b\xe8\xbd\xbd\xe5\x90\x8d\xe7\xa7\xb0')),
                ('dramaname', models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x89\xa7\xe9\x9b\x86\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('starturl', models.TextField(max_length=1000, null=True, verbose_name=b'\xe8\xb5\xb7\xe5\xa7\x8b\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('dramatype', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\x89\xa7\xe9\x9b\x86\xe7\xb1\xbb\xe5\x9e\x8b', blank=True)),
            ],
        ),
    ]
