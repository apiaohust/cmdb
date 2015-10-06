#coding:utf-8
__author__ = 'lenovo'

from django.conf.urls import patterns, include, url
from cmdb import views

urlpatterns = patterns('',
     url(r'^$', views.index, name='index'),
     url(r'^cm_os/(?P<serverid>[\w\-]+)/add_os/$',views.add_os, name='add_os'),
     url(r'^cm_os/$', views.cm_os, name='cm_os'),
     #服务器增删改查
     url(r'^add_server/$',views.add_server,name='add_server'),#添加服务器
     url(r'^server/$', views.server, name='server'),#全查服务器信息
     url(r'^query_server/$', views.query_server, name='query_server'),#分页查询服务器
     url(r'^remove_server/$', views.remove_server, name='remove_server'),#删除服务器
     url(r'^get_edit_server/$', views.get_edit_server, name='get_edit_server'),#获取编辑行信息-服务器
     url(r'^edit_server/$', views.edit_server, name='edit_server'),#更新服务器
     #操作系统
)
