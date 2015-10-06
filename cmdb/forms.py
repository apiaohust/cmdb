#coding:utf-8
__author__ = 'lenovo'
from django import forms
import datetime
from cmdb.models import CM_SERVER,CM_OS,CM_DATABASE,CM_MIDWARE,CM_APP,CM_VCLUSTER,CM_PUBPLATFORM
from django.forms.widgets import Widget, Select, MultiWidget
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User


class OSForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput,initial=0)
    number = forms.CharField(max_length=50, label="编号",help_text="input number")
    type = forms.CharField(max_length=50,label="类型",help_text="input type")
    version = forms.CharField(max_length=50,label="版本",help_text="input version")
    create_time= forms.DateField(widget=SelectDateWidget(years=range(1990,2050,1),), label="安装时间")
    disk_content=forms.IntegerField()
    memory = forms.IntegerField()
    class Meta:
        model = CM_OS
        fields=('number','type','version','create_time','disk_content','memory','id')


class ServerForm(forms.ModelForm):
   id = forms.IntegerField(widget=forms.HiddenInput,initial=0)
   hardware_num = forms.CharField(max_length=50,required=False )
   architecture = forms.CharField(max_length=50,required=False)
   version = forms.CharField(max_length=50,required=False)
   cpu_count = forms.IntegerField(required=False)
   memory = forms.IntegerField(required=False)
   detail = forms.CharField(max_length=700,required=False)
   fun_name = forms.CharField(max_length=100,required=False)
   admin_ip = forms.CharField(max_length=100,required=False)
   server_ip = forms.CharField(max_length=100,required=False)
   net_local = forms.CharField(max_length=50,required=False)
   vcluster = forms.IntegerField(required=False)
   m_room = forms.CharField(max_length=70,required=False)
   m_cabinet = forms.CharField(max_length=50,required=False)
   m_cabloc = forms.CharField(max_length=50,required=False)
   buy_time = forms.DateField(required=False)
   set_time = forms.DateField(required=False)
   monitor = forms.CharField(max_length=100,required=False)
   datebase = forms.IntegerField(required=False)
    #TODO
   midleware = forms.IntegerField(required=False)
   HA = forms.CharField(max_length=50,required=False)
   status = forms.CharField(max_length=50,required=False)
   ex_store =  forms.CharField(max_length=50,required=False)
   ex_miya =  forms.CharField(max_length=50,required=False)

   class Meta:
       model = CM_SERVER
       fields = ('hardware_num','architecture','version','memory','cpu_count','detail','id','fun_name','admin_ip','server_ip','net_local',
                'vcluster','m_room','m_cabinet','m_cabloc','buy_time','set_time','monitor','datebase','midleware','HA','status','ex_store','ex_miya')


class DatabaseForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput,initial=0)
    soft_num = forms.CharField(max_length=70)
    custom_name = forms.CharField(max_length=70)
    database_type = forms.CharField(max_length=70)
    database_version = forms.CharField(max_length=70)
    application = forms.CharField(max_length=70)
    class Meta:
       model = CM_DATABASE
       fields = ('soft_num','custom_name','database_type','database_version','application','id')