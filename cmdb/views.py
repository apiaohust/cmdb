# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from cmdb.models import CM_SERVER, CM_DATABASE, CM_OS, CM_MIDWARE, CM_APP, CM_PUBPLATFORM, CM_VCLUSTER
from cmdb.forms import OSForm, ServerForm, DatabaseForm, MidwareForm, AppForm, PubForm, VclusterForm
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required

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
    # 数据转换为int类型
    rows = int(request.GET["rows"])
    page = int(request.GET["page"])
    firstpage = (page - 1) * rows
    lastpage = page * rows
    serverlist = CM_SERVER.objects.all()[firstpage:lastpage]  # 从数据库查询服务器信息
    servertotal = CM_SERVER.objects.count()  # 返回总行数
    temp = list(serverlist.values())
    dict_server = {"total": servertotal, "rows": temp}
    result = json.dumps(dict_server, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="application/json")


'''
    增加-页面add_server.html
    返回server.html
'''


# z增加数据
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
    return render(request, 'cmdb/add_server.html', {'form': form})


# 返回到server.xml
@login_required
def server(request):
    server_list = CM_SERVER.objects.all()
    result = serializers.serialize("json", server_list)
    context_dict = {'serverlist': result}
    return render(request, 'cmdb/server.html', context_dict)


'''
    删除
    页面server.xml
    参数：id
    返回 页面server.xml
'''


# server_remove
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


# 获取当前行信息
def get_edit_server(request):
    r_id = request.GET["id"]
    result = CM_SERVER.objects.get(id=r_id)
    form = ServerForm(instance=result)
    return render(request, 'cmdb/edit_server.html', {'form': form})


# update
def edit_server(request):
    if request.method == 'POST':
        r_id = request.POST["id"]
        server_info = CM_SERVER.objects.get(id=r_id)  # 获取要更改行
        form = ServerForm(request.POST, instance=server_info)
        if form.is_valid():
            form.save()
            return server(request)
        else:
            print form.errors
    else:
        form = ServerForm()
    return render(request, 'cmdb/add_server.html', {'form': form})


'''
     get_midware_list
'''


def get_midware_list(request):
    print request.GET["id"]
    r_id = int(request.GET["id"])
    midwarelist = CM_REL_SERVER_MIDWARE.objects.filter(server_id=r_id)

    return HttpResponse(r_id)


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
    # 数据转换为int类型
    rows = int(request.GET["rows"])
    page = int(request.GET["page"])
    firstpage = (page - 1) * rows
    lastpage = page * rows
    oslist = CM_OS.objects.all()[firstpage:lastpage]  # 从数据库查询服务器信息
    ostotal = CM_OS.objects.count()  # 返回总行数
    temp = list(oslist.values())
    dict_os = {"total": ostotal, "rows": temp}
    result = json.dumps(dict_os, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="application/json")


def os(request):
    os_list = CM_OS.objects.all()
    result = serializers.serialize("json", os_list)
    context_dict = {'oslist': result}
    return render(request, 'cmdb/os.html', context_dict)


'''
    增加-页面add_os.html
    返回os.html
'''


# z增加os数据
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
    return render(request, 'cmdb/add_os.html', {'form': form})


'''
    删除
    页面os.xml
    参数：id
    返回 页面os.xml
'''


# server_remove
def remove_os(request):
    r_id = request.GET["id"]
    result = CM_OS.objects.get(id=r_id)
    result.delete()
    return HttpResponse("success")


'''
    编辑
    页面：os.html
    参数id
    页面：edit_os.html
    参数：form
    返回页面  edit_os.html
'''


# 获取当前行信息
def get_edit_os(request):
    r_id = request.GET["id"]
    result = CM_OS.objects.get(id=r_id)
    form = OSForm(instance=result)
    return render(request, 'cmdb/edit_os.html', {'form': form})


# update
def edit_os(request):
    if request.method == 'POST':
        r_id = request.POST["id"]
        os_info = CM_OS.objects.get(id=r_id)  # 获取要更改行
        form = OSForm(request.POST, instance=os_info)
        if form.is_valid():
            form.save()
            return os(request)
        else:
            print form.errors
    else:
        form = OSForm()
    return render(request, 'cmdb/add_os.html', {'form': form})


'''
数据库

查询-页面db.html
获取参数：rows 每页行数  page 当前页
根据当前页，每页大小获取数据db
返回db.html
'''


def query_db(request):
    # 数据转换为int类型
    rows = int(request.GET["rows"])
    page = int(request.GET["page"])
    firstpage = (page - 1) * rows
    lastpage = page * rows
    dblist = CM_DATABASE.objects.all()[firstpage:lastpage]  # 从数据库查询服务器信息
    dbtotal = CM_DATABASE.objects.count()  # 返回总行数
    temp = list(dblist.values())
    dict_db = {"total": dbtotal, "rows": temp}
    result = json.dumps(dict_db, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="application/json")


'''
    增加-页面add_db.html
    返回db.html
'''


# z增加数据
def add_db(request):
    if request.method == 'POST':
        form = DatabaseForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return db(request)
        else:
            print form.errors
    else:
        form = DatabaseForm()
    return render(request, 'cmdb/add_db.html', {'form': form})


# 返回到db.html
def db(request):
    db_list = CM_DATABASE.objects.all()
    result = serializers.serialize("json", db_list)
    context_dict = {'dblist': result}
    return render(request, 'cmdb/db.html', context_dict)


'''
    删除
    页面db.html
    参数：id
    返回 页面db.html
'''


# db_remove
def remove_db(request):
    r_id = request.GET["id"]
    result = CM_DATABASE.objects.get(id=r_id)
    result.delete()
    return HttpResponse("success")


'''
    编辑
    页面：db.html
    参数id
    页面：edit_db.html
    参数：form
    返回页面  edit_db.html
'''


# 获取当前行信息
def get_edit_db(request):
    r_id = request.GET["id"]
    result = CM_DATABASE.objects.get(id=r_id)
    form = DatabaseForm(instance=result)
    return render(request, 'cmdb/edit_db.html', {'form': form})


# update
def edit_db(request):
    if request.method == 'POST':
        r_id = request.POST["id"]
        db_info = CM_DATABASE.objects.get(id=r_id)  # 获取要更改行
        form = DatabaseForm(request.POST, instance=db_info)
        if form.is_valid():
            form.save()
            return db(request)
        else:
            print form.errors
    else:
        form = DatabaseForm()
    return render(request, 'cmdb/add_db.html', {'form': form})


'''
中间件

查询-页面midware.html
获取参数：rows 每页行数  page 当前页
根据当前页，每页大小获取数据midware
返回midware.html
'''


def query_midware(request):
    # 数据转换为int类型
    rows = int(request.GET["rows"])
    page = int(request.GET["page"])
    firstpage = (page - 1) * rows
    lastpage = page * rows
    midwarelist = CM_MIDWARE.objects.all()[firstpage:lastpage]  # 从数据库查询服务器信息
    midwaretotal = CM_MIDWARE.objects.count()  # 返回总行数
    temp = list(midwarelist.values())
    dict_midware = {"total": midwaretotal, "rows": temp}
    result = json.dumps(dict_midware, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="application/json")


'''
    增加-页面add_midware.html
    返回midware.html
'''


# z增加数据
def add_midware(request):
    if request.method == 'POST':
        form = MidwareForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return midware(request)
        else:
            print form.errors
    else:
        form = MidwareForm()
    return render(request, 'cmdb/add_midware.html', {'form': form})


# 返回到db.html
def midware(request):
    midware_list = CM_MIDWARE.objects.all()
    result = serializers.serialize("json", midware_list)
    context_dict = {'midwarelist': result}
    return render(request, 'cmdb/midware.html', context_dict)


'''
    删除
    页面midware.html
    参数：id
    返回 页面midware.html
'''


# db_remove
def remove_midware(request):
    r_id = request.GET["id"]
    result = CM_MIDWARE.objects.get(id=r_id)
    result.delete()
    return HttpResponse("success")


'''
    编辑
    页面：midware.html
    参数id
    页面：edit_midware.html
    参数：form
    返回页面  edit_midware.html
'''


# 获取当前行信息
def get_edit_midware(request):
    r_id = request.GET["id"]
    result = CM_MIDWARE.objects.get(id=r_id)
    form = MidwareForm(instance=result)
    return render(request, 'cmdb/edit_midware.html', {'form': form})


# update
def edit_midware(request):
    if request.method == 'POST':
        r_id = request.POST["id"]
        midware_info = CM_MIDWARE.objects.get(id=r_id)  # 获取要更改行
        form = MidwareForm(request.POST, instance=midware_info)
        if form.is_valid():
            form.save()
            return midware(request)
        else:
            print form.errors
    else:
        form = MidwareForm()
    return render(request, 'cmdb/add_midware.html', {'form': form})


'''
APP

查询-页面app.html
获取参数：rows 每页行数  page 当前页
根据当前页，每页大小获取app数据
返回app.html
'''


def query_app(request):
    # 数据转换为int类型
    rows = int(request.GET["rows"])
    page = int(request.GET["page"])
    firstpage = (page - 1) * rows
    lastpage = page * rows
    applist = CM_APP.objects.all()[firstpage:lastpage]  # 从数据库查询服务器信息
    apptotal = CM_APP.objects.count()  # 返回总行数
    temp = list(applist.values())
    dict_app = {"total": apptotal, "rows": temp}
    result = json.dumps(dict_app, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="application/json")


'''
    增加-页面add_app.html
    返回app.html
'''


# z增加数据
def add_app(request):
    if request.method == 'POST':
        form = AppForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return app(request)
        else:
            print form.errors
    else:
        form = AppForm()
    return render(request, 'cmdb/add_app.html', {'form': form})


# 返回到server.xml
def app(request):
    app_list = CM_APP.objects.all()
    result = serializers.serialize("json", app_list)
    context_dict = {'applist': result}
    return render(request, 'cmdb/app.html', context_dict)


'''
    删除
    页面app.xml
    参数：id
    返回 页面app.xml
'''


# server_remove
def remove_app(request):
    r_id = request.GET["id"]
    result = CM_APP.objects.get(id=r_id)
    result.delete()
    return HttpResponse("success")


'''
    编辑
    页面：app.html
    参数id
    页面：edit_app.html
    参数：form
    返回页面  edit_app.html
'''


# 获取当前行信息
def get_edit_app(request):
    r_id = request.GET["id"]
    result = CM_APP.objects.get(id=r_id)
    form = AppForm(instance=result)
    return render(request, 'cmdb/edit_app.html', {'form': form})


# update
def edit_app(request):
    if request.method == 'POST':
        r_id = request.POST["id"]
        app_info = CM_APP.objects.get(id=r_id)  # 获取要更改行
        form = AppForm(request.POST, instance=app_info)
        if form.is_valid():
            form.save()
            return app(request)
        else:
            print form.errors
    else:
        form = AppForm()
    return render(request, 'cmdb/add_app.html', {'form': form})


'''
虚拟集群

查询-页面vcluster.html
获取参数：rows 每页行数  page 当前页
根据当前页，每页大小获取vcluster数据
返回vcluster.html
'''


def query_vcluster(request):
    # 数据转换为int类型
    rows = int(request.GET["rows"])
    page = int(request.GET["page"])
    firstpage = (page - 1) * rows
    lastpage = page * rows
    vclusterlist = CM_VCLUSTER.objects.all()[firstpage:lastpage]  # 从数据库查询服务器信息
    vclustertotal = CM_VCLUSTER.objects.count()  # 返回总行数
    temp = list(vclusterlist.values())
    dict_vcluster = {"total": vclustertotal, "rows": temp}
    result = json.dumps(dict_vcluster, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="application/json")


'''
    增加-页面add_vcluster.html
    返回vcluster.html
'''


# z增加数据
def add_vcluster(request):
    if request.method == 'POST':
        form = VclusterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return vcluster(request)
        else:
            print form.errors
    else:
        form = VclusterForm()
    return render(request, 'cmdb/add_vcluster.html', {'form': form})


# 返回到server.xml
def vcluster(request):
    vcluster_list = CM_VCLUSTER.objects.all()
    result = serializers.serialize("json", vcluster_list)
    context_dict = {'vclusterlist': result}
    return render(request, 'cmdb/vcluster.html', context_dict)


'''
    删除
    页面vcluster.xml
    参数：id
    返回 页面vcluster.xml
'''


# server_remove
def remove_vcluster(request):
    r_id = request.GET["id"]
    result = CM_VCLUSTER.objects.get(id=r_id)
    result.delete()
    return HttpResponse("success")


'''
    编辑
    页面：vcluster.html
    参数id
    页面：edit_vcluster.html
    参数：form
    返回页面  edit_vcluster.html
'''


# 获取当前行信息
def get_edit_vcluster(request):
    r_id = request.GET["id"]
    result = CM_VCLUSTER.objects.get(id=r_id)
    form = VclusterForm(instance=result)
    return render(request, 'cmdb/edit_vcluster.html', {'form': form})


# update
def edit_vcluster(request):
    if request.method == 'POST':
        r_id = request.POST["id"]
        vcluster_info = CM_VCLUSTER.objects.get(id=r_id)  # 获取要更改行
        form = VclusterForm(request.POST, instance=vcluster_info)
        if form.is_valid():
            form.save()
            return vcluster(request)
        else:
            print form.errors
    else:
        form = VclusterForm()
    return render(request, 'cmdb/add_vcluster.html', {'form': form})


'''
公共平台 pub

查询-页面pub.html
获取参数：rows 每页行数  page 当前页
根据当前页，每页大小获取pub数据
返回pub.html
'''


def query_pub(request):
    # 数据转换为int类型
    rows = int(request.GET["rows"])
    page = int(request.GET["page"])
    firstpage = (page - 1) * rows
    lastpage = page * rows
    publist = CM_PUBPLATFORM.objects.all()[firstpage:lastpage]  # 从数据库查询服务器信息
    pubtotal = CM_PUBPLATFORM.objects.count()  # 返回总行数
    temp = list(publist.values())
    dict_pub = {"total": pubtotal, "rows": temp}
    result = json.dumps(dict_pub, cls=DjangoJSONEncoder)
    return HttpResponse(result, content_type="application/json")


'''
    增加-页面add_pub.html
    返回pub.html
'''


# z增加数据
def add_pub(request):
    if request.method == 'POST':
        form = PubForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return pub(request)
        else:
            print form.errors
    else:
        form = PubForm()
    return render(request, 'cmdb/add_pub.html', {'form': form})


# 返回到server.xml
def pub(request):
    pub_list = CM_PUBPLATFORM.objects.all()
    result = serializers.serialize("json", pub_list)
    context_dict = {'publist': result}
    return render(request, 'cmdb/pub.html', context_dict)


'''
    删除
    页面server.xml
    参数：id
    返回 页面server.xml
'''


# server_remove
def remove_pub(request):
    r_id = request.GET["id"]
    result = CM_PUBPLATFORM.objects.get(id=r_id)
    result.delete()
    return HttpResponse("success")


'''
    编辑
    页面：pub.html
    参数id
    页面：edit_pub.html
    参数：form
    返回页面  edit_pub.html
'''


# 获取当前行信息
def get_edit_pub(request):
    r_id = request.GET["id"]
    result = CM_PUBPLATFORM.objects.get(id=r_id)
    form = PubForm(instance=result)
    return render(request, 'cmdb/edit_pub.html', {'form': form})


# update
def edit_pub(request):
    if request.method == 'POST':
        r_id = request.POST["id"]
        pub_info = CM_PUBPLATFORM.objects.get(id=r_id)  # 获取要更改行
        form = PubForm(request.POST, instance=pub_info)
        if form.is_valid():
            form.save()
            return pub(request)
        else:
            print form.errors
    else:
        form = PubForm()
    return render(request, 'cmdb/add_pub.html', {'form': form})


def index(request):
    os_list = CM_OS.objects.all()
    context_dict = {'oslist': os_list}
    return render(request, 'cmdb/index.html', context_dict)


def cm_os(request):
    os_list = CM_OS.objects.all()
    context_dict = {'oslist': os_list}
    return render(request, 'cmdb/os.html', context_dict)


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
