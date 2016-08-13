# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from twisted.enterprise import adbapi
from hashlib import md5
import MySQLdb
import MySQLdb.cursors
import time

class MySQLStoreVnscPipeline(object):
    def __init__(self):
 
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            host = '',
            db = 'recoder',
            user = 'recoder',
            passwd = '',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = True
        )
    

    #pipeline默认调用
    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._do_insert, item, spider) 
        d.addErrback(self._handle_error, item, spider)
        return d

    #将每行更新或写入数据库中
    def _do_insert(self, conn, item, spider):
        linkmd5id="%s_%s"%(item['title'],item['episode'])
        conn.execute('select 1 from spider_taskinfo where linkmd5id = "%s"'%linkmd5id)
        ret = conn.fetchone()
        stime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()) 
        if not ret:
            conn.execute('insert into spider_taskinfo(linkmd5id, dramaurl, episode, downloadurl, downloadstatus,stime) values("%s", "%s", "%s", "%s", 0 ,"%s")'%(linkmd5id, item['htmlurl'], item['episode'], item['downloadurl'],stime))

    #异常处理
    def _handle_error(self, failue, item, spider):
        pass
