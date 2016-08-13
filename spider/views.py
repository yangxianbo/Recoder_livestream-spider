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
from spider.models import *

def get_starturl(request):
    startlist=taskmain.objects.all().values_list('starturl','dramatype')
    return_dict={'drama':[],'movie':[]}
    for obj in startlist:
        if obj[1] == "vn_movie":
            return_dict['movie'].append(obj[0])
        else:
            return_dict['drama'].append(obj[0])
    return HttpResponse(json.dumps(return_dict ,indent=4,ensure_ascii=False), 'application/javascript')

@login_required()
def spider_index(request, template_name):
    queryset=taskmain.objects.all().order_by('-id')
    search_fields = ['dirpath']
    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
        })

@login_required()
def add_taskmain(request):
    try:
        dirpath=request.POST['dirpath']
        dramaname=request.POST['dramaname']
        starturl=request.POST['starturl']
        dramatype=request.POST['dramatype']
        new=taskmain.objects.create(dirpath=dirpath,dramaname=dramaname,starturl=starturl,dramatype=dramatype)
        new.save()
        return HttpResponse('ok')
    except Exception,e:
        return HttpResponse(e)

@login_required()
def update_taskmain(request):
    try:
        pk=request.POST['pk']
        dirpath=request.POST['dirpath']
        dramaname=request.POST['dramaname']
        starturl=request.POST['starturl']
        dramatype=request.POST['dramatype']
        taskmain.objects.filter(pk=pk).update(dirpath=dirpath,dramaname=dramaname,starturl=starturl,dramatype=dramatype)
        return HttpResponse('ok')
    except Exception,e:
        return HttpResponse(e)

@login_required()
def del_taskmain(request):
    pk=request.POST['pk']
    tids = [ int(i) for i in pk.split(',') ]
    if len(tids) > 0:
        taskmain.objects.filter(id__in=tids).delete()
    return HttpResponse('ok')

@login_required()
def task_info(request, template_name):
    _keyword = request.REQUEST.get('keyword', "0")
    _taskstatus = request.REQUEST.get('taskstatus', "9")
    if _keyword != "0" and _taskstatus == "9":
        starttime = request.GET['start_time']
        endtime = request.GET['end_time']
        _t = request.REQUEST.get('t', "today")
        queryset=taskinfo.objects.filter(dramaurl__contains=_keyword,stime__range=[starttime,endtime]).order_by("-id")
    elif _keyword != "0" and _taskstatus != "9":
        starttime = request.GET['start_time']
        endtime = request.GET['end_time']
        _t = request.REQUEST.get('t', "today")
        queryset=taskinfo.objects.filter(dramaurl__contains=_keyword,stime__range=[starttime,endtime],downloadstatus=_taskstatus).order_by("-id")
    else:pass

    search_fields = ['episode']
    return get_datatables_records(
        request,
        queryset,
        search_fields,
        template_name,
        extra_context={
            't':_t,
            'u_stime':starttime,
            'u_etime':endtime,
            'keyword':_keyword,
            'taskstatus':_taskstatus
        })

