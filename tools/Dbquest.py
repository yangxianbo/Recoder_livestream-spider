#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-06-21 18:30:21
#FILENAME: Dbquest.py
#DESCRIPTION: 
#===============================================================

import MySQLdb
import urllib2
import urllib
import sys,os
import ConfigParser

reload(sys)
sys.setdefaultencoding('utf-8')

def post_info(url,postinfo):
    jdata = urllib.urlencode(postinfo)
    req = urllib2.urlopen(url, jdata)
    return req.read()

def dbquest(sql):
    try:
        path="/www/Recoder/tools/config.ini"
        if not os.path.exists(path):
            sys.exit("找不到配置文件:%s" % path)
        cf = ConfigParser.ConfigParser()
        cf.read(path)
        user=cf.get('db_config','user')
        passwd=cf.get('db_config','passwd')
        host=cf.get('db_config','host')
        db=cf.get('db_config','db')
        conn=MySQLdb.connect(host=host,db=db,user=user,passwd=passwd,charset='utf8')
        cur=conn.cursor()
        cur.execute(sql)
        _sql=cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return _sql
    except Exception:
        return -1

