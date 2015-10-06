#coding:utf-8
__author__ = 'lenovo'
from django import forms
import datetime
from cmdb.models import CM_SERVER,CM_OS,CM_DATABASE
from django.forms.widgets import Widget, Select, MultiWidget
from django.forms.extras.widgets import SelectDateWidget


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
   hardware_num = forms.CharField(max_length=50 )
   architecture = forms.CharField(max_length=50)
   version = forms.CharField(max_length=50)
   cpu_count = forms.IntegerField()
   memory = forms.IntegerField()
   detail = forms.CharField(max_length=700)
   class Meta:
       model = CM_SERVER
       fields = ('hardware_num','architecture','version','memory','cpu_count','detail','id')


class DatabaseForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput,initial=0)
    soft_num = forms.CharField(max_length=70, blank=True)
    custom_name = forms.CharField(max_length=70, blank=True)
    database_type = forms.CharField(max_length=70, blank=True)
    database_version = forms.CharField(max_length=70, blank=True)
    application = forms.CharField(max_length=70, blank=True)
    class Meta:
       model = CM_DATABASE
       fields = ('soft_num','custom_name','database_type','database_version','application','id')