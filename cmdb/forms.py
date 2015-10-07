# coding:utf-8
__author__ = 'lenovo'
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput
from cmdb.models import CM_SERVER, CM_OS, CM_DATABASE, CM_MIDWARE, CM_APP, CM_VCLUSTER, CM_PUBPLATFORM,CM_CONFIG


class OSForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    #server = forms.IntegerField(label="关联服务器")
    number = forms.CharField(max_length=50, label="编号", help_text="input number")
    type = forms.CharField(max_length=50, label="类型", help_text="input type")
    version = forms.CharField(max_length=50, label="版本", help_text="input version")
    create_time = forms.DateField(widget=SelectDateWidget(years=range(1990, 2050, 1), ), label="安装时间")
    disk_content = forms.IntegerField(label="磁盘空间")
    memory = forms.IntegerField(label="内存")

    class Meta:
        model = CM_OS
        fields = ('number', 'type', 'version', 'create_time', 'disk_content', 'memory', 'id')


class ServerForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    hardware_num = forms.CharField(max_length=50, required=False, label="硬件编号")
    architecture = forms.CharField(max_length=50, required=False,label="架构类型")
    version = forms.CharField(max_length=50, required=False,label="版本")
    cpu_count = forms.IntegerField(required=False,label="cpu数量")
    memory = forms.IntegerField(required=False,label="内存大小")
    detail = forms.CharField(max_length=700, required=False,label="详情")
    fun_name = forms.CharField(max_length=100, required=False,label="功能名称")
    admin_ip = forms.CharField(max_length=100, required=False,label="管理ip")
    server_ip = forms.CharField(max_length=100, required=False,label="服务ip")
    net_local = forms.CharField(max_length=50, required=False,label="网络位置")
    vcluster = forms.IntegerField(required=False,label="所属集群")
    m_room = forms.CharField(max_length=70, required=False,label="机房位置")
    m_cabinet = forms.CharField(max_length=50, required=False,label="机柜")
    m_cabloc = forms.CharField(max_length=50, required=False,label="机柜位")
    buy_time = forms.DateField(widget=SelectDateWidget(years=range(1990, 2050, 1), ), label="入库时间")
    set_time = forms.DateField(widget=SelectDateWidget(years=range(1990, 2050, 1), ), label="安装时间")
    monitor = forms.CharField(max_length=100, required=False,label="监控名称")
    datebase = forms.IntegerField(required=False,label="数据库")
    # TODO
    midleware = forms.IntegerField(required=False,label="中间件")
    HA = forms.CharField(max_length=50, required=False,label="高可用类型")
    status = forms.CharField(max_length=50, required=False,label="服务器状态")
    ex_store = forms.CharField(max_length=50, required=False,label="外连存储")
    ex_miya = forms.CharField(max_length=50, required=False,label="外连密押")

    class Meta:
        model = CM_SERVER
        fields = (
        'hardware_num', 'architecture', 'version', 'memory', 'cpu_count', 'detail', 'id', 'fun_name', 'admin_ip',
        'server_ip', 'net_local',
        'vcluster', 'm_room', 'm_cabinet', 'm_cabloc', 'buy_time', 'set_time', 'monitor', 'datebase', 'midleware', 'HA',
        'status', 'ex_store', 'ex_miya')


class DatabaseForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    soft_num = forms.CharField(max_length=70)
    custom_name = forms.CharField(max_length=70)
    database_type = forms.CharField(max_length=70)
    database_version = forms.CharField(max_length=70)
    application = forms.CharField(max_length=70)

    class Meta:
        model = CM_DATABASE
        fields = ('soft_num', 'custom_name', 'database_type', 'database_version', 'application', 'id')


class MidwareForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    solf_num = forms.CharField(max_length=70)
    custom_name = forms.CharField(max_length=70)
    mid_type = forms.CharField(max_length=70)
    mid_name = forms.CharField(max_length=70)

    class Meta:
        model = CM_MIDWARE
        fields = ('solf_num', 'custom_name', 'mid_type', 'mid_name', 'id')


class AppForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    apply_num = forms.CharField(max_length=70)
    base_info = forms.CharField(max_length=100)
    system_status = forms.CharField(max_length=70)
    dev_strategy = forms.CharField(max_length=70)

    class Meta:
        model = CM_APP
        fields = ('apply_num', 'base_info', 'system_status', 'dev_strategy', 'id')


class VclusterForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    hard_num = forms.CharField(max_length=70)
    cluster_name = forms.CharField(max_length=70)
    cluster_type = forms.CharField(max_length=70)
    cluster_solft = forms.CharField(max_length=70)
    soft_version = forms.CharField(max_length=70)
    net_local = forms.CharField(max_length=70)

    class Meta:
        model = CM_VCLUSTER
        fields = ('hard_num', 'cluster_name', 'cluster_type', 'cluster_solft', 'id', 'soft_version', 'net_local')


class PubForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    soft_num = forms.CharField(max_length=70)
    cluster_name = forms.CharField(max_length=70)
    cluster_type = forms.CharField(max_length=70)
    cluster_soft = forms.CharField(max_length=70)
    soft_version = forms.CharField(max_length=70)
    net_local = forms.CharField(max_length=70)

    class Meta:
        model = CM_PUBPLATFORM
        fields = ('soft_num', 'cluster_name', 'cluster_type', 'cluster_soft', 'id', 'soft_version', 'net_local')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ConfigForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    config_name = forms.CharField(max_length=70)
    remark = forms.CharField(max_length=100)
    class Meta:
        model = CM_CONFIG
        fields = ('config_name', 'remark', 'id')

