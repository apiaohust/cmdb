# coding:utf-8
__author__ = 'lenovo'

from django.conf.urls import patterns, url
from cmdb import views
from cmdb import authview,autoviews

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       # url(r'^cm_os/(?P<serverid>[\w\-]+)/add_os/$',views.add_os, name='add_os'),
                       url(r'^cm_os/$', views.cm_os, name='cm_os'),
                       # 服务器增删改查
                       url(r'^add_server/$', views.add_server, name='add_server'),  # 添加服务器
                       url(r'^server/$', views.server, name='server'),  # 全查服务器信息
                       url(r'^query_server/$', views.query_server, name='query_server'),  # 分页查询服务器
                       url(r'^remove_server/$', views.remove_server, name='remove_server'),  # 删除服务器
                       url(r'^get_edit_server/$', views.get_edit_server, name='get_edit_server'),  # 获取编辑行信息-服务器
                       url(r'^edit_server/$', views.edit_server, name='edit_server'),  # 更新服务器
                       url(r'^server_get_midwarelist/$', views.server_get_midwarelist, name='server_get_midwarelist'),  # 更新服务器
                       url(r'^server_get_midwarelist_html/$', views.server_get_midwarelist_html, name='server_get_midwarelist_html'),  # 更新服务器

                       # 操作系统
                       url(r'^query_os/$', views.query_os, name='query_os'),  # 分页查询os
                       url(r'^os/$', views.os, name='os'),  # 全查os信息
                       url(r'^add_os/$', views.add_os, name='add_os'),  # 添加os
                       url(r'^remove_os/$', views.remove_os, name='remove_os'),  # 删除os
                       url(r'^get_edit_os/$', views.get_edit_os, name='get_edit_os'),  # 获取编辑行信息-os
                       url(r'^edit_os/$', views.edit_os, name='edit_os'),  # 更新os
                       # 数据库
                       url(r'^query_db/$', views.query_db, name='query_db'),  # 分页查询数据库
                       url(r'^db/$', views.db, name='db'),  # 全查数据库信息
                       url(r'^add_db/$', views.add_db, name='add_db'),  # 添加数据库
                       url(r'^remove_db/$', views.remove_db, name='remove_db'),  # 删除数据库
                       url(r'^get_edit_db/$', views.get_edit_db, name='get_edit_db'),  # 获取编辑行信息-数据库
                       url(r'^edit_db/$', views.edit_db, name='edit_db'),  # 更新数据库
                       # 中间件
                       url(r'^query_midware/$', views.query_midware, name='query_midware'),  # 分页查询数据库
                       url(r'^midware/$', views.midware, name='midware'),  # 全查数据库信息
                       url(r'^add_midware/$', views.add_midware, name='add_midware'),  # 添加数据库
                       url(r'^remove_midware/$', views.remove_midware, name='remove_midware'),  # 删除数据库
                       url(r'^get_edit_midware/$', views.get_edit_midware, name='get_edit_midware'),  # 获取编辑行信息-数据库
                       url(r'^edit_midware/$', views.edit_midware, name='edit_midware'),  # 更新数据库
                       # 应用
                       url(r'^query_app/$', views.query_app, name='query_app'),  # 分页查询应用
                       url(r'^app/$', views.app, name='app'),  # 全查应用信息
                       url(r'^add_app/$', views.add_app, name='add_app'),  # 添加应用
                       url(r'^remove_app/$', views.remove_app, name='remove_app'),  # 删除应用
                       url(r'^get_edit_app/$', views.get_edit_app, name='get_edit_app'),  # 获取编辑行信息-应用
                       url(r'^edit_app/$', views.edit_app, name='edit_app'),  # 更新应用
                       # 虚拟集群
                       url(r'^query_vcluster/$', views.query_vcluster, name='query_vcluster'),  # 分页查询虚拟集群
                       url(r'^vcluster/$', views.vcluster, name='vcluster'),  # 全查虚拟集群信息
                       url(r'^add_vcluster/$', views.add_vcluster, name='add_vcluster'),  # 添加虚拟集群
                       url(r'^remove_vcluster/$', views.remove_vcluster, name='remove_vcluster'),  # 删除虚拟集群
                       url(r'^get_edit_vcluster/$', views.get_edit_vcluster, name='get_edit_vcluster'),  # 获取编辑行信息-虚拟集群
                       url(r'^edit_vcluster/$', views.edit_vcluster, name='edit_vcluster'),  # 更新虚拟集群
                       # 公共平台
                       url(r'^query_pub/$', views.query_pub, name='query_pub'),  # 分页查询公共平台
                       url(r'^pub/$', views.pub, name='pub'),  # 全查公共平台信息
                       url(r'^add_pub/$', views.add_pub, name='add_pub'),  # 添加公共平台
                       url(r'^remove_pub/$', views.remove_pub, name='remove_pub'),  # 删除公共平台
                       url(r'^get_edit_pub/$', views.get_edit_pub, name='get_edit_pub'),  # 获取编辑行信息-公共平台
                       url(r'^edit_pub/$', views.edit_pub, name='edit_pub'),  # 更新公共平台
                       #配置项
                       url(r'^query_config/$', views.query_config, name='query_config'),  # 分页查询配置项
                       url(r'^config/$', views.config, name='config'),  # 全查配置项信息
                       url(r'^add_config/$', views.add_config, name='add_config'),  # 添加配置项
                       url(r'^remove_config/$', views.remove_config, name='remove_config'),  # 删除配置项
                       url(r'^get_edit_config/$', views.get_edit_config, name='get_edit_config'),  # 获取编辑行信息-配置项
                       url(r'^edit_config/$', views.edit_config, name='edit_config'),  # 更新配置项

                       url(r'^register/$', authview.register, name='register'),
                       url(r'^login/$', authview.user_login, name='login'),
                       url(r'^logout/$', authview.user_logout, name='logout'),

                       ##自动更新
                       url(r'^upserver/$', autoviews.updateServer, name='upserver'),
                       )
