#coding:utf-8
#通用类
import os, sys, commands, re, time, json
from django.shortcuts import render_to_response, get_object_or_404, render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core import serializers
from django.template import RequestContext, loader, Context
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.http import HttpResponse
from django.contrib import admin
from account.decorator import login_required
from django.http import Http404
from django.db.models import Q
#tools
from tools.utils import get_datatables_records,UnixTime,time_change_stime,timestamp,stime_change_time,getip
#models
from luzhi.models import *

@login_required()
def playsource_index(request, template_name):
    queryset=channel.objects.all().order_by('channelid')
    search_fields = ['channelid','channelname']
    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
        })

@login_required()
def add_source(request):
    try:
        channelid=request.POST['cid']
        channelname=request.POST['cname']
        channelurl=request.POST['url']
        offset=request.POST['offset']
        new=channel.objects.create(channelid=channelid,channelname=channelname,channelurl=channelurl,offset=offset)
        new.save()
        return HttpResponse('ok')
    except Exception,e:
        return HttpResponse(e)

@login_required()
def update_source(request):
    try:
        pk=request.POST['pk']
        channelid=request.POST['cid']
        channelname=request.POST['cname']
        channelurl=request.POST['url']
        offset=request.POST['offset']
        channel.objects.filter(pk=pk).update(channelid=channelid,channelname=channelname,channelurl=channelurl,offset=offset)
        return HttpResponse('ok')
    except Exception,e:
        return HttpResponse(e)

@login_required()
def del_source(request):
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        channel.objects.filter(id__in=tids).delete()
    return HttpResponse('ok')

@login_required()
def task_log(request, template_name):
    _pid = request.REQUEST.get('channelid', "0")
    _taskstatus = request.REQUEST.get('taskstatus', "9")
    if _pid != "0" and _taskstatus == "9":
        starttime = request.GET['start_time']
        endtime = request.GET['end_time']
        _t = request.REQUEST.get('t', "today")
        cname=channel.objects.get(channelid=_pid).channelname
        queryset=channel_task.objects.filter(channelid=_pid,stime__range=[starttime,endtime]).order_by('stime')
    elif _pid != "0" and _taskstatus != "9":
        starttime = request.GET['start_time']
        endtime = request.GET['end_time']
        _t = request.REQUEST.get('t', "today")
        cname=channel.objects.get(channelid=_pid).channelname
        queryset=channel_task.objects.filter(channelid=_pid,stime__range=[starttime,endtime],taskstatus=_taskstatus).order_by('stime')
    else:pass

    search_fields = ['locatename']
    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
            't':_t,
            'u_stime':starttime,
            'u_etime':endtime,
            'channelid':_pid,
            'channelname':cname,
            'taskstatus':_taskstatus
        })


