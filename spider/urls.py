#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-07-13 10:53:20
#FILENAME: urls.py
#DESCRIPTION: 
#===============================================================


from django.conf.urls import include, url, patterns

urlpatterns = patterns('spider.views',
    url(r'^getstart$', 'get_starturl', name='getstart_url'),
    url(r'^addtaskmain$', 'add_taskmain', name='add_taskmain'),
    url(r'^updatetaskmain$', 'update_taskmain', name='update_taskmain'),
    url(r'^deltaskmain$', 'del_taskmain', name='del_taskmain'),
    url(r'^taskmain/$', 'spider_index', {'template_name':'main_index.html'}, name='spider_index'),
    url(r'^taskinfo/$', 'task_info', {'template_name':'task_info.html'}, name='task_info'),
)
