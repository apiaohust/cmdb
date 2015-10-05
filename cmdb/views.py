from django.shortcuts import render
from django.http import HttpResponse
from cmdb.models import CM_SERVER
from cmdb.models import CM_OS
from cmdb.forms import OSForm
from cmdb.forms import ServerForm
from cmdb.forms import ServerForm


def index(request):
    os_list = CM_OS.objects.all()
    context_dict  = {'oslist':os_list}

    return render(request,'cmdb/index.html', context_dict )

def server(request):
    server_list = CM_SERVER.objects.all()
    context_dict  = {'serverlist':server_list}

    return render(request,'cmdb/server.html', context_dict )

def cm_os(request):
    os_list = CM_OS.objects.all()
    context_dict  = {'oslist':os_list}
    return render(request,'cmdb/os.html', context_dict )

def add_server(request):
    if request.method == 'POST':
        form = ServerForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
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




