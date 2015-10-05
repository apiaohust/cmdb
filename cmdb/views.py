#utf-8
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




def index(request):
    os_list = CM_OS.objects.all()
    context_dict  = {'oslist':os_list}
    return render(request,'cmdb/index.html', context_dict )

def server(request):
    server_list = CM_SERVER.objects.all()
    result = serializers.serialize("json", server_list)
    context_dict = {'serverlist':result}
    return render(request,'cmdb/server.html', context_dict)

def get_json1(request):
    server_list = CM_SERVER.objectsall()
    dict = {"row1":"1","total":server_list}
    result = json.dumps(dict)
    return render_to_response(request,result, context_instance=RequestContext(request))


#server_remove
def server_remove(request):
    r_id = request.GET["id"]
    result = CM_SERVER.objects.get(id=r_id)
    result.delete()
    return HttpResponse("delete success")

def get_json(request):
    serverlist = CM_SERVER.objects.all()
    server_total = CM_SERVER.objects.count()
    print  server_total
    print serverlist.values()
    aa = list(serverlist.values())
    #bb = json.loads(aa)
    #result1 = serializers.serialize("json",serverlist)
    #print result1
    #templist = json.loads(result1)
    cc = {"tatal":server_total,"rows":aa}
    result = json.dumps(cc)
    return  HttpResponse(result,content_type="application/json")




def test(request):
   return render_to_response("cmdb/server.html")

def cm_os(request):
    os_list = CM_OS.objects.all()
    context_dict  = {'oslist':os_list}
    return render(request,'cmdb/os.html', context_dict )

#add_server
def add_server(request):
    print 1
    print request.POST
    print 2
    print request.GET["id"]
    print 3
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




