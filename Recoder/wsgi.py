#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-05-03 10:35:11
#FILENAME: wsgi.py
#DESCRIPTION: 
#===============================================================


import os,sys

if not os.path.dirname(__file__) in sys.path[:1]:
    sys.path.insert(0, os.path.dirname(__file__))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
