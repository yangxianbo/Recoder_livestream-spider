#coding:utf-8
from django.db import models

# Create your models here.
class taskmain(models.Model):
    dirpath=models.CharField('目录以及下载名称',max_length=255,unique=True)
    dramaname=models.CharField('剧集名称',max_length=255,null=True,blank=True)
    starturl=models.TextField('起始地址',max_length=1000,null=True,blank=True)
    dramatype=models.CharField('剧集类型',max_length=50,null=True,blank=True)

class taskinfo(models.Model):
    dramaurl=models.TextField('爬取地址',max_length=1000,null=True,blank=True)
    episode=models.CharField('集数',max_length=50,null=True,blank=True)
    downloadurl=models.TextField('下载地址',max_length=1000,null=True,blank=True)
    linkmd5id=models.CharField('唯一ID',max_length=255,null=True,blank=True)
    downloadstatus=models.CharField('下载状态',max_length=5,null=True,blank=True)
    stime=models.DateTimeField('任务抓取时间',auto_now_add=False,null=True,blank=True)
    etime=models.DateTimeField('下载完成时间',auto_now_add=False,null=True,blank=True)
