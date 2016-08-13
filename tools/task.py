#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-06-21 15:22:51
#FILENAME: task.py
#DESCRIPTION: 
#===============================================================


import os,sys,commands
import logging, time
import socket
import json
import subprocess,signal
import psutil
import ConfigParser
from Dbquest import dbquest
from Dbquest import post_info

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
ffmpeg=cf.get('base_path','ffmpeg')
notifyurl_1=cf.get('cms_url','notifyurl_1')
notifyurl_2=cf.get('cms_url','notifyurl_2')
luzhitmp=cf.get('luzhi_tmp','path')
luzhipath=cf.get('luzhi_path','path')

#日志模块
if not os.path.exists(logpath): os.system('mkdir -p %s'%logpath)
logging.basicConfig(filename = '%s/%s.log' %(logpath,unix_te()), level = logging.DEBUG, filemode = 'a', format = '%(asctime)s - %(levelname)s: %(message)s')

def quest_url(channelid):
    sql='select channelurl from luzhi_channel where channelid=%s'%channelid
    dbreturn=dbquest(sql)
    if dbreturn != ():
        return dbreturn[0][0]
    else:return -1

def insert_id(locatename,taskid):
    sql='update luzhi_channel_task set taskid="%s" where locatename="%s";'%(taskid,locatename)
    try:
        dbreturn=dbquest(sql)
        return 0
    except Exception:
        return -1

def get_id(locatename):
    sql='select taskid from luzhi_channel_task where locatename="%s";'%locatename
    dbreturn=dbquest(sql)
    if dbreturn != ():
        return dbreturn[0][0]
    else:return -1

def update_status(locatename,status,filepath):
    sql='update luzhi_channel_task set taskstatus="%s",filepath="%s.ts" where locatename="%s";'%(status,filepath,locatename)
    try:
        dbreturn=dbquest(sql)
        return 0
    except Exception:
        return -1

def assemble_json(locatename):
    sql='select channelid,taskname,date_format(stime,"%%Y-%%m-%%d %%H:%%i:%%s"),date_format(etime,"%%Y-%%m-%%d %%H:%%i:%%s") from luzhi_channel_task where locatename="%s";'%locatename
    dbreturn=dbquest(sql)
    if dbreturn != ():
        return dbreturn[0]
    else:return -1

if __name__ == "__main__" :
    if len(sys.argv[1:]) >= 1:
        locatename=sys.argv[1]
        mode=sys.argv[2]
        channelid=locatename.split('_')[0]
        if mode == "start":
            url=quest_url(channelid)
            if url != -1 and url != '':
                p=subprocess.Popen('nohup %s -y -i %s -vcodec copy -acodec copy %s/%s.ts &'%(ffmpeg,url,luzhitmp,locatename),shell=True,close_fds=True,bufsize=-1,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                p.wait()
                time.sleep(1)
                taskid=commands.getoutput("ps aux|grep ffmpeg|grep %s.ts|grep -v grep|awk '{print $2}'"%locatename)
                insert_id(locatename,taskid)
                update_status(locatename,0,0)
                logging.info("task:%s start,pid:%s"%(locatename,taskid))
        elif mode == "stop":
#            taskid=get_id(locatename)
            taskid=commands.getoutput("ps aux|grep ffmpeg|grep %s.ts|grep -v grep|awk '{print $2}'"%locatename)
            if taskid != -1 and taskid != '':
                try:
                    psutil.Process(int(taskid))
                    os.system('kill -9 %s'%taskid)
#                    os.kill(int(taskid),signal.SIGKILL)
                    os.system('mv %s/%s.ts %s/'%(luzhitmp,locatename,luzhipath))
                    update_status(locatename,2,'%s/%s'%(luzhipath,locatename))
                    sqltup=assemble_json(locatename)
                    if sqltup != -1:
                        cid=sqltup[0]
                        tname=sqltup[1]
                        stime=sqltup[2]
                        etime=sqltup[3]
                        fname="%s/%s.ts"%(luzhipath,locatename)
#                        postinfo="channelid=%s&videoname=%s&starttime=%s&endtime=%s&filename=%s"%(cid,tname,stime,etime,fname)
                        postinfo={'channelid':cid,'videoname':tname,'starttime':stime,'endtime':etime,'filename':fname}
                        post_info(notifyurl_1,postinfo)
                        post_info(notifyurl_2,postinfo)
                        logging.info("task:%s is stop,info:%s"%(locatename,postinfo))
                    os.system('kill -9 %s'%taskid)
#                    os.kill(int(taskid),signal.SIGKILL)
                except psutil.NoSuchProcess:
                    logging.error("task:%s is failed"%locatename)
            else:
                update_status(locatename,-1,0)
                logging.error("task:%s is failed"%locatename)
