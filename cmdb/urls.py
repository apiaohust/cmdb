#utf-8
__author__ = 'lenovo'

from django.conf.urls import patterns, include, url
from cmdb import views

urlpatterns = patterns('',
     url(r'^$', views.index, name='index'),
     url(r'^cm_os/(?P<serverid>[\w\-]+)/add_os/$',views.add_os, name='add_os'),
     url(r'^cm_os/$', views.cm_os, name='cm_os'),
     url(r'^add_server/$',views.add_server,name='add_server'),
     url(r'^server/$', views.server, name='server'),
     url(r'^get_json/$', views.get_json, name='get_json'),
     url(r'^test/$', views.test, name='test'),
     url(r'^server_remove/$', views.server_remove, name='server_remove'),
)
