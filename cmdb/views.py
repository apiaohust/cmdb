#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from cmdb.models import CM_SERVER
from cmdb.models import CM_OS
from cmdb.forms import OSForm
from cmdb.forms import ServerForm
import json
from django.core import serializers
from django.shortcuts import render_to_response
from collections import defaultdict
from collections import OrderedDict
from django.template import RequestContext
from django.core.serializers.json import DjangoJSONEncoder

'''
    样例：增删查改--以服务器管理为例
'''
'''
查询-页面server.html
获取参数：rows 每页行数  page 当前页
根据当前页，每页大小获取server数据
返回server.html
'''
def query_server(request):
    #数据转换为int类型
    rows = int(request.GET["rows"])
    page = int(request.GET["page"])
    firstpage = (page-1) * rows
    lastpage =  page * rows
    serverlist = CM_SERVER.objects.all()[firstpage:lastpage]  #从数据库查询服务器信息
    servertotal = CM_SERVER.objects.count()  #返回总行数
    temp = list(serverlist.values())
    dict_server = {"total":servertotal,"rows":temp}
    result = json.dumps(dict_server,cls=DjangoJSONEncoder)
    return  HttpResponse(result,content_type="application/json")

'''
    增加-页面add_server.html
    返回server.html
'''
#z增加数据
def add_server(request):
    if request.method == 'POST':
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return server(request)
        else:
            print form.errors
    else:
        form = ServerForm()
    return render(request,'cmdb/add_server.html',{'form':form})
#返回到server.xml
def server(request):
    server_list = CM_SERVER.objects.all()
    result = serializers.serialize("json", server_list)
    context_dict = {'serverlist':result}
    return render(request,'cmdb/server.html', context_dict)

'''
    删除
    页面server.xml
    参数：id
    返回 页面server.xml
'''
#server_remove
def remove_server(request):
    r_id = request.GET["id"]
    result = CM_SERVER.objects.get(id=r_id)
    result.delete()
    return HttpResponse("success")
'''
    编辑
    页面：server.html
    参数id
    页面：edit_server.html
    参数：form
    返回页面  edit_server.html
'''

#获取当前行信息
def get_edit_server(request):
    r_id = request.GET["id"]
    result = CM_SERVER.objects.get(id=r_id)
    form = ServerForm(instance=result)
    return render(request,'cmdb/edit_server.html',{'form':form})

#update
def edit_server(request):
    if request.method == 'POST':
        r_id = request.POST["id"]
        server_info = CM_SERVER.objects.get(id=r_id) #获取要更改行
        form = ServerForm(request.POST, instance=server_info)
        if form.is_valid():
            form.save()
            return server(request)
        else:
            print form.errors
    else:
        form = ServerForm()
    return render(request,'cmdb/add_server.html',{'form':form})

'''
    服务器增删查改结束
'''

'''
    操作系统
'''
'''
查询-页面os.html
获取参数：rows 每页行数  page 当前页
根据当前页，每页大小获取server数据
返回os.html
'''
def query_os(request):
    #数据转换为int类型
    rows = int(request.GET["rows"])
    page = int(request.GET["page"])
    firstpage = (page-1) * rows
    lastpage =  page * rows
    oslist = CM_OS.objects.all()[firstpage:lastpage]  #从数据库查询服务器信息
    ostotal = CM_OS.objects.count()  #返回总行数
    temp = list(oslist.values())
    dict_server = {"total":ostotal,"rows":temp}
    result = json.dumps(dict_server,cls=DjangoJSONEncoder)
    return  HttpResponse(result,content_type="application/json")

def os(request):
    os_list = CM_OS.objects.all()
    result = serializers.serialize("json", os_list)
    context_dict = {'oslist':result}
    return render(request,'cmdb/os.html', context_dict)


'''
    增加-页面add_os.html
    返回os.html
'''
#z增加os数据
def add_os(request):
    if request.method == 'POST':
        form = OSForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return os(request)
        else:
            print form.errors
    else:
        form = OSForm()
    return render(request,'cmdb/add_os.html',{'form':form})

'''
    删除
    页面server.xml
    参数：id
    返回 页面server.xml
'''
#server_remove
def remove_os(request):
    r_id = request.GET["id"]
    result = CM_OS.objects.get(id=r_id)
    result.delete()
    return HttpResponse("success")
'''
    编辑
    页面：server.html
    参数id
    页面：edit_server.html
    参数：form
    返回页面  edit_server.html
'''

#获取当前行信息
def get_edit_os(request):
    r_id = request.GET["id"]
    result = CM_OS.objects.get(id=r_id)
    form = OSForm(instance=result)
    return render(request,'cmdb/edit_os.html',{'form':form})

#update
def edit_os(request):
    if request.method == 'POST':
        r_id = request.POST["id"]
        os_info = CM_OS.objects.get(id=r_id) #获取要更改行
        form = OSForm(request.POST, instance=os_info)
        if form.is_valid():
            form.save()
            return os(request)
        else:
            print form.errors
    else:
        form = OSForm()
    return render(request,'cmdb/add_os.html',{'form':form})



























def index(request):
    os_list = CM_OS.objects.all()
    context_dict  = {'oslist':os_list}
    return render(request,'cmdb/index.html', context_dict )

def cm_os(request):
    os_list = CM_OS.objects.all()
    context_dict  = {'oslist':os_list}
    return render(request,'cmdb/os.html', context_dict)

'''
def add_os(request, serverid):
    try:
        server = CM_SERVER.objects.get(id=serverid)
    except CM_SERVER.DoesNotExist:
        server = None

    if request.method == 'POST':
        form = OSForm(request.POST)
        if form.is_valid():
            if server:
                cm_os = form.save(commit =False)
                cm_os.server =server
                cm_os.save()
                form.save(commit=True)
                return index(request)
        else:
            print form.errors
    else:
        form = OSForm()
        context_dict = {'form':form,'server':server}
    return render(request,'cmdb/add_os.html', context_dict)
'''




