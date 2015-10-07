__author__ = 'lenovo'
from django.shortcuts import render
from django.http import HttpResponse
from cmdb.models import CM_SERVER, CM_DATABASE, CM_OS, CM_MIDWARE, CM_APP, CM_PUBPLATFORM, CM_VCLUSTER
from cmdb.forms import OSForm, ServerForm, DatabaseForm, MidwareForm, AppForm, PubForm, VclusterForm
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
import urllib
import urllib2


def updateServer(request):
    id = request.GET["id"]
    server = CM_SERVER.objects.get(id=id)
    # if  "linux" in result.architecture.lower() or "aix" in
    # print server.id
    serverinfo = getServerDate(ip="").get('data').get('serverinfo').get('data')
    print serverinfo
    server.admin_ip =serverinfo.get('server_ip')
    server.architecture = serverinfo.get('server_arch')
    server.cpu_count = serverinfo.get('cpuTotal')
    server.detail =serverinfo.get('server_detail')
    server.memory = serverinfo.get('MemTotal')
    server.server_ip = serverinfo.get('server_ip')
    server.version = serverinfo.get('server_detail')[3]
    # server = CM_SERVER(admin_ip=serverinfo.get('server_ip'),architecture = serverinfo.get('server_arch'),
    #                    cpu_count = serverinfo.get('cpuTotal'),detail =serverinfo.get('server_detail'),
    #                    memory = serverinfo.get('MemTotal'),server_ip = serverinfo.get('server_ip'),
    #                    version = serverinfo.get('server_detail')[3])
    server.save()
    return HttpResponse("success")

def upOS(request):
    id = request.GET["id"]
    cm_os = CM_OS.objects.get(id=id)
    os_info = getServerDate(ip="").get('data').get('sysinfo').get('data')
    cm_os.version = os_info.get('sys_version')
    cm_os.memory = os_info.get()
    cm_os.disk_content = os_info.get()

def getServerDate(ip):
    #url =  "http://"+ip + "8655/getdata" \
    url = "http://127.0.0.1:8655/getdata"
    req = urllib2.urlopen(url)
    test = req.read()
    return json.loads(test)
