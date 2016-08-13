#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-06-24 09:41:00
#FILENAME: test.py
#DESCRIPTION: 
#===============================================================


from Dbquest import dbquest
#from Dbquest import post_info
import urllib
import urllib2
import json	
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def post_info(url,postinfo):
#    jdata = json.dumps(postinfo)
    jdata = urllib.urlencode(postinfo)
    req = urllib2.urlopen(url, jdata)
#    req = urllib2.Request(url, postinfo)
#    response = urllib2.urlopen(req)
    return req.read()

def assemble_json(locatename):
    sql='select channelid,taskname,date_format(stime,"%%Y-%%m-%%d %%H:%%i:%%s"),date_format(etime,"%%Y-%%m-%%d %%H:%%i:%%s") from luzhi_channel_task where locatename="%s";'%locatename
    dbreturn=dbquest(sql)
    if dbreturn != ():
        return dbreturn[0]
    else:return -1

locatename="567_201606230130"
sqltup=assemble_json(locatename)
if sqltup != -1:
    cid=sqltup[0]
    tname=sqltup[1]
    stime=sqltup[2]
    etime=sqltup[3]
    fname="/data/luzhi_new/%s.ts"%locatename
    postinfo={'channelid':cid,'videoname':tname,'starttime':stime,'endtime':etime,'filename':fname}
#    postinfo='channelid=%s&videoname=%s&starttime=%s&endtime=%s&filename=%s'%(cid,tname,stime,etime,fname)
#    postjson="json=%s"%urllib.quote(json.dumps(postinfo))
#    postjson=urllib.quote(postinfo)
    url='http://cc.krway.cc:9015/Api/Notifysucess'
#    post_info(url,postjson)
    post_info(url,postinfo)
