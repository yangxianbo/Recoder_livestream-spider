#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-03-15 18:35:30
#FILENAME: download.py
#DESCRIPTION: 
#===============================================================

import urllib,urllib2 
import os,sys,json,time
import socket
import ConfigParser
import multiprocessing
from Dbquest import dbquest

socket.setdefaulttimeout(10)

# 设置默认编码为utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

path="/www/Recoder/tools/config.ini"
if not os.path.exists(path):
    sys.exit("找不到配置文件:%s" % path)
cf = ConfigParser.ConfigParser()
cf.read(path)
basepath=cf.get('base_path','download')

def download(url,episode,path,taskid):
    downloadpath="%s/%s"%(basepath,path)
    downloadname="%s/%s/%s_%s.mp4"%(basepath,path,path,episode)
    if not os.path.exists(downloadpath):
        os.system('mkdir -p %s'%downloadpath)
    try:
        sql2='update spider_taskinfo set downloadstatus=2  where id=%s'%taskid
        dbquest(sql2)
        d_info=urllib.urlretrieve(url,downloadname)
        total=int(d_info[-1]['Content-Length'])
        localsize=os.path.getsize(downloadname)
        etime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        if int(localsize) >= int(total) and int(localsize) > 2500000:
            sql='update spider_taskinfo set downloadstatus=1 etime="%s" where id=%s'%(etime,taskid)
            dbquest(sql)
            return 0
        else:
            sql='update spider_taskinfo set downloadstatus=0  where id=%s'%taskid
            dbquest(sql)
            os.system('rm -f %s'%downloadname)
            return -1
    except Exception,e:
        sql='update spider_taskinfo set downloadstatus=0  where id=%s'%taskid
        dbquest(sql)
        os.system('rm -f %s'%downloadname)
        return -1

class Download():
    
    def _gettask(self):
        sql='select dirpath from spider_taskmain'
        dirlist=dbquest(sql)
        taskmain=[]
        for dirname in dirlist:
            pertask=self._gettaskinfo(dirname[0])
            taskmain=list(set(taskmain).union(set(pertask)))
        return taskmain
        

    def _gettaskinfo(self,dirname):
        sql='select downloadurl,episode,id from spider_taskinfo where dramaurl like "%%%s%%" and downloadstatus=0'%dirname
        tasklist=dbquest(sql)
        return_list=[]
        for task in tasklist:
            return_list.append((task[0],task[1],dirname,task[2]))
        return return_list


    def _multidownload(self,taskmain):
        #------------multiprocess--------------#
        pool = multiprocessing.Pool(processes=5)
        for task in taskmain:
            pool.apply_async(download, (task[0],task[1],task[2],task[3], ))
        pool.close()
        pool.join()
        #------------multiprocess--------------#

    def main(self):
        taskmain=self._gettask()
        self._multidownload(taskmain)

if __name__ == '__main__':
    command = "ps -ef|grep %s|grep -v grep" % os.path.basename(__file__)
    if len(os.popen(command).readlines()) > 1:
        print 'exit'
        sys.exit(1)
    d=Download() 
    d.main()
