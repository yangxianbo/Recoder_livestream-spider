#coding:utf-8
from django.db import models

# Create your models here.
class channel(models.Model):
    channelid=models.CharField('频道ID',max_length=255,unique=True)
    channelname=models.CharField('频道名称',max_length=255,null=True,blank=True)
    channelurl=models.CharField('源地址',max_length=255,null=True,blank=True)
    offset=models.CharField('偏移量',max_length=5,default='0')

class channel_task(models.Model):
    channelid=models.CharField('频道ID',max_length=255)
    locatename=models.CharField('任务唯一ID',max_length=255,unique=True)
    taskname=models.CharField('任务名称',max_length=255,null=True,blank=True)
    taskid=models.CharField('任务进程ID',max_length=5,default='1')
    stime=models.DateTimeField('任务开始时间',auto_now_add=False)
    etime=models.DateTimeField('任务结束时间',auto_now_add=False)
    taskstatus=models.CharField('任务状态',max_length=5,default='1')
    filepath=models.CharField('视频地址',max_length=255,null=True,blank=True)
