#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-07-14 16:42:59
#FILENAME: getinfo.py
#DESCRIPTION: 
#===============================================================


import urllib
import urllib2
import json
import httplib
from Dbquest import dbquest

def get_info(url):
    try:
        req=urllib.urlopen(url)
        code=req.getcode()
        return json.loads(req.read())
    except Exception:
        return -1

if __name__ == "__main__":
    url="http://admins.quliebiao.com:9022/Force/Spider"
    task_list=get_info(url)
    if task_list != -1:
        for task in task_list:
            name=task['name']
            dtype=task['type']
            starturl=task['drama']
            dirpath=task['root_dir']
            sql='insert into spider_taskmain(dirpath,dramaname,dramatype,starturl) values("%s","%s","%s","%s")'%(dirpath,name,dtype,starturl)
            dbquest(sql)
