#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-06-27 11:12:52
#FILENAME: empty.py
#DESCRIPTION: 
#===============================================================


import time,os,commands,sys
import ConfigParser
import psutil


def stime_change_time(t):
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(float(t)))


def check_timeout(pid,today):
    today=stime_change_time(today).split(' ')[0]
    p=psutil.Process(int(pid))
    startday=stime_change_time(p.create_time()).split(' ')[0]
    if startday != today:
        os.system('kill -9 %s'%pid)
    else:
        pass

def scan_file(path,today,deleteday):
    _FILE_=[]
    path=path.rstrip('/')
    for  root,dirs,files in os.walk(path):
        for filename in files:
            filepath=os.path.join(root,filename)
            create_time=os.path.getctime(filepath)
            passday=int((today-create_time)/86400)
            if passday >= int(deleteday):
                _FILE_.append(os.path.join(root,filename))
    return _FILE_

if __name__ == '__main__':
    #配置文件
    path="/www/Recoder/tools/config.ini"
    if not os.path.exists(path):
        sys.exit("找不到配置文件:%s" % path)
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    basepath=cf.get('base_path','path')
    sys.path.append(basepath)
    cronfile=cf.get('cron_file','filepath')
    luzhitmp=cf.get('luzhi_tmp','path')
    luzhipath=cf.get('luzhi_path','path')
    deleteday=cf.get('delete_day','time')
    today=time.time()

    #执行每日初始化
    pidlist=commands.getoutput("ps aux|grep ffmpeg|grep -v grep|awk '{print $2}'").split('\n')
    if pidlist != ['']:
        for pid in pidlist:
            check_timeout(pid,today)
    #防止未终结任务,重复执行一次
    pidlist=commands.getoutput("ps aux|grep ffmpeg|grep -v grep|awk '{print $2}'").split('\n')
    if pidlist != ['']:
        for pid in pidlist:
            check_timeout(pid,today)

    #清空计划任务
    os.system("/bin/sed -i '/task/d' %s"%cronfile)

    #删除临时文件
    os.system("/bin/rm -f %s/*"%luzhitmp)

    #删除超过期限的文件
    filelist=scan_file(luzhipath,today,deleteday)
    for filepath in filelist:
        os.system('rm -f %s'%filepath)
