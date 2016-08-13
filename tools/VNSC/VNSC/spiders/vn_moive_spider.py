#!/usr/bin/python2.7
#coding:utf-8
#AUTHOR: yangxb
#CREATER: 2016-07-08 15:20:26
#FILENAME: vn_spider.py
#DESCRIPTION: 
#===============================================================


from scrapy.spider import Spider 
from scrapy.http import Request 
from scrapy.selector import Selector
from VNSC.items import VnscItem
import re

import urllib
import urllib2
import json
import httplib

def get_info(url):
    req=urllib.urlopen(url)
    code=req.getcode()
    return json.loads(req.read())

class VnSpider(Spider):
    name = "hphim_movie"
    allowed_domains = ["hphim.net"]
    start_urls = get_info('http://recoder.quliebiao.com:9898/spider/getstart')['movie']


    def parse(self,response):
        item = VnscItem()
        urllist=response.xpath('//script/text()').extract()
        p=re.compile(r'.*?label:\"480p\" \}\,\{file\:\"(.*?video\.mp4)\"\, type\:\"mp4\"\, label\:\"360p\".*?')
        for urlfind in urllist:
            url=p.findall(urlfind)
            if len(url) != 0:
                item['downloadurl']=url[0]
        item['episode']=1
        item['title']=response.xpath('//span[@class="title-1"]/text()').extract()[0]
        item['htmlurl']=response.url
        yield item
