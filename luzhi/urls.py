#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-06-20 11:37:41
#FILENAME: urls.py
#DESCRIPTION: 
#===============================================================

from django.conf.urls import include, url, patterns

urlpatterns = patterns('luzhi.views',
    url(r'^addsource$', 'add_source', name='add_source'),
    url(r'^updatesource$', 'update_source', name='update_source'),
    url(r'^delsource$', 'del_source', name='del_source'),
    url(r'^source/$', 'playsource_index', {'template_name':'source_index.html'}, name='playsource_index'),
    url(r'^task/$', 'task_log', {'template_name':'task_index.html'}, name='task_log'),
)
