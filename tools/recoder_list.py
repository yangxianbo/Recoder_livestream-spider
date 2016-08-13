#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-06-20 10:51:55
#FILENAME: recoder_list.py
#DESCRIPTION: 
#===============================================================


import re,sys,os
import logging, time
import urllib
import json
import httplib
import socket
import ConfigParser
from Dbquest import dbquest

socket.setdefaulttimeout(180)

# 设置默认编码为utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

def unix_te(day=0):
    return time.strftime(
        '%Y-%m-%d',
        time.localtime(time.time()-86400*day)
    )

path="/www/Recoder/tools/config.ini"
if not os.path.exists(path):
    sys.exit("找不到配置文件:%s" % path)
cf = ConfigParser.ConfigParser()
cf.read(path)
logpath=cf.get('log_path','path')
cronfile=cf.get('cron_file','filepath')
python=cf.get('base_path','python')
basepath=cf.get('base_path','path')
taskurl=cf.get('cms_url','taskurl')
offset=cf.get('offset','time')
#日志模块
if not os.path.exists(logpath): os.system('mkdir -p %s'%logpath)
logging.basicConfig(filename = '%s/%s.log' %(logpath,unix_te()), level = logging.DEBUG, filemode = 'a', format = '%(asctime)s - %(levelname)s: %(message)s')

#get消息
def get_info(url):
    req=urllib.urlopen(url)
    code=req.getcode()
    return json.loads(req.read())

#读取计划任务
def read_cront(filename):
    readtmp=[]
    taskinfo={}
    with open(filename,"r") as read1:
        for line in read1:
            line=line.strip('\n')
            p=re.compile(r'(\d*\s\d*)\s\*\s*\s*.*?task\.py\s(\S*\s\S*)')
            find=p.findall(line)
            if len(find) != 0:
                readtmp.append(find[0])

    for tup in readtmp:
        timetup=tup[0].split(' ')
        tasktup=tup[1].split(' ')
        taskid=tasktup[0].split('_')[0]
        taskmode=tasktup[1]
        mintime=timetup[0]
        hourtime=timetup[1]
        task='%s:%s_%s'%(hourtime,mintime,taskmode)
        if not taskinfo.has_key(taskid):
            taskinfo[taskid]=[]
        taskinfo[taskid].append(task)
    return taskinfo


#写入计划任务
class Task():
    def __init__(self,gettask,otime):
        self.gettask=gettask
        self.offset=otime
        self.filename=cronfile
        self.readcache=read_cront(self.filename)
        
    def _check_task(self):
        for taskall in self.gettask:
            channelid=taskall['id']
            tasklist=taskall['content']
            daytime=taskall['time']
            localtime=time.strftime('%Y-%m-%d',time.localtime(time.time()))
            if daytime == localtime:
                for task in tasklist:
                    try:
                        taskname=task['name']
                        starttime=task['starttime']
                        endtime=task['endtime']
                        #计算偏移量
                        stup=starttime.split(':')
                        etup=endtime.split(':')
                        smintime=int(stup[0])*60+int(stup[1])+int(self.offset)
                        starth=smintime/60
                        if int(starth) < 10:
                            starth="0%s"%starth
                        startm=smintime%60
                        if int(startm) < 10:
                            startm="0%s"%startm
                        emintime=int(etup[0])*60+int(etup[1])+int(self.offset)+2
                        endh=emintime/60
                        if int(endh) < 10:
                            endh="0%s"%endh
                        endm=emintime%60
                        if int(endm) < 10:
                            endm="0%s"%endm
                        cachestask="%s:%s_start"%(starth,startm)
                        cacheetask="%s:%s_stop"%(endh,endm)
                        if self.readcache.has_key(channelid):
                            if cachestask not in self.readcache[channelid] or cacheetask not in self.readcache[channelid]:
                                self._insert_task(daytime,channelid,taskname,starth,startm,endh,endm,starttime,endtime)
                        else:
                            self._insert_task(daytime,channelid,taskname,starth,startm,endh,endm,starttime,endtime)
                    except Exception:
                        pass

    def _insert_task(self,daytime,channelid,taskname,starth,startm,endh,endm,sqlstime,sqletime):
        sqlstime="%s %s:00"%(daytime,sqlstime)
        sqletime="%s %s:00"%(daytime,sqletime)
        locatename="%s_%s%s%s"%(channelid,daytime.replace('-',''),starth,startm)
        stime="%s %s:%s:00"%(daytime,starth,startm)
        etime="%s %s:%s:00"%(daytime,endh,endm)
        insertsql='insert into luzhi_channel_task(channelid,locatename,taskname,taskid,stime,etime,taskstatus) values("%s","%s","%s","1","%s","%s","1");'%(channelid,locatename,taskname,sqlstime,sqletime)
        if not dbquest(insertsql) == -1:
            os.system('echo "%s %s * * * %s %s/task.py %s start" >>%s'%(startm,starth,python,basepath,locatename,self.filename))
            logging.info("channel:%s insert task success,starttime %s:%s"%(channelid,starth,startm))

            os.system('echo "%s %s * * * %s %s/task.py %s stop" >>%s'%(endm,endh,python,basepath,locatename,self.filename))
            logging.info("channel:%s insert task success,locatename: %s,endtime %s:%s"%(channelid,locatename,endh,endm))
    def main(self):
        self._check_task()


if __name__ == '__main__':
    gettask=get_info(taskurl)
    a=Task(gettask,int(offset))
    a.main()
