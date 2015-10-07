# coding:utf-8
from django.db import models
from django.contrib.auth.models import User


## 服务器
class CM_SERVER(models.Model):
    id = models.AutoField(primary_key=True)  # 自增id
    pub_platform = models.ForeignKey('CM_PUBPLATFORM')  # 外键关联公共平台 n:1
    hardware_num = models.CharField(max_length=50, blank=True)  # 硬件编号
    architecture = models.CharField(max_length=50, blank=True)  # 架构类型
    version = models.CharField(max_length=50, blank=True)  # 版本
    cpu_count = models.IntegerField()  # cpu数量
    memory = models.IntegerField()  # 内存大小
    detail = models.CharField(max_length=700, blank=True)  # 详情
    fun_name = models.CharField(max_length=100, blank=True)  # 功能名称
    admin_ip = models.CharField(max_length=100, blank=True)  # 管理ip
    server_ip = models.CharField(max_length=100, blank=True)  # 服务ip
    net_local = models.CharField(max_length=50, blank=True)  # 网络位置
    vcluster = models.IntegerField()  # 所属集群
    m_room = models.CharField(max_length=70, blank=True)  # 机房位置
    m_cabinet = models.CharField(max_length=50, blank=True)  # 机柜
    m_cabloc = models.CharField(max_length=50, blank=True)  # 机柜位
    buy_time = models.DateField()  # 入库时间
    set_time = models.DateField()  # 安装时间
    monitor = models.CharField(max_length=100, blank=True)  # 监控名称
    # TODO
    datebase = models.IntegerField()
    # TODO
    midleware = models.IntegerField()
    HA = models.CharField(max_length=50, blank=True)  # 高可用类型
    status = models.CharField(max_length=50, blank=True)  # 服务器状态
    ex_store = models.CharField(max_length=50, blank=True)  # 外连存储
    ex_miya = models.CharField(max_length=50, blank=True)  # 外连密押

    def __unicode__(self):
        return self.id


# 操作系统
class CM_OS(models.Model):
    id = models.AutoField(primary_key=True, blank=True)  # 自增主键
    server = models.ForeignKey('CM_SERVER')  # 外键关联服务器 n:1
    number = models.CharField(max_length=50, blank=True)  # 编号
    type = models.CharField(max_length=50, blank=True)  # 类型
    version = models.CharField(max_length=50, blank=True)  # 版本
    create_time = models.DateField()  # 安装时间
    disk_content = models.IntegerField()  # 磁盘空间
    memory = models.IntegerField()  # 内存

    def __unicode__(self):
        return self.id


##应用系统
class CM_APP(models.Model):
    id = models.AutoField(primary_key=True)  # 自增ID
    apply_num = models.CharField(max_length=70, blank=True)  # 应用编号
    base_info = models.CharField(max_length=100, blank=True)  # 基本信息
    system_status = models.CharField(max_length=70, blank=True)  # 系统状态
    dev_strategy = models.CharField(max_length=70, blank=True)  # 开发策略
    first_field = models.CharField(max_length=70, blank=True)  # 一级域
    second_field = models.CharField(max_length=70, blank=True)  # 二级域
    tech_depart = models.CharField(max_length=70, blank=True)  # 科技部门
    app_admin = models.CharField(max_length=70, blank=True)  # 应用负责人
    yw_depart = models.CharField(max_length=70, blank=True)  # 业务部门
    yw_admin = models.CharField(max_length=70, blank=True)  # 业务负责人
    op_level = models.CharField(max_length=70, blank=True)  # 运维等级
    server_time = models.CharField(max_length=70, blank=True)  # 服务时间
    zaibei_status = models.CharField(max_length=70, blank=True)  # 是否建立灾备
    is_opensource = models.CharField(max_length=70, blank=True)  # 源码是否开放
    RTO = models.CharField(max_length=70, blank=True)
    RPO = models.CharField(max_length=70, blank=True)

    def __unicode__(self):
        return self.apply_num


##虚拟集群

class CM_VCLUSTER(models.Model):
    id = models.AutoField(primary_key=True)  # 自增ID
    hard_num = models.CharField(max_length=70, blank=True)  # 硬件编号
    cluster_name = models.CharField(max_length=70, blank=True)  # 集群名称
    cluster_type = models.CharField(max_length=70, blank=True)  # 集群类型
    cluster_solft = models.CharField(max_length=70, blank=True)  # 集群软件
    soft_version = models.CharField(max_length=70, blank=True)  # 软件版本
    net_local = models.CharField(max_length=70, blank=True)  # 网络位置
    # TODO
    server = models.CharField(max_length=70, blank=True)  # 外键关联服务器
    create_time = models.DateField()  # 创建时间

    def __unicode__(self):
        return self.id


##中间件
class CM_MIDWARE(models.Model):
    id = models.AutoField(primary_key=True)  # 自增主键
    pub_platform = models.ForeignKey('CM_PUBPLATFORM')  # 外键关联公共平台
    server = models.ForeignKey('CM_SERVER')  # 外键关联服务器
    solf_num = models.CharField(max_length=70, blank=True)  # 软件编号
    custom_name = models.CharField(max_length=70, blank=True)  # 自定义名称
    mid_type = models.CharField(max_length=70, blank=True)  # 中间类型
    mid_name = models.CharField(max_length=70, blank=True)  # 中间件名称
    mid_version = models.CharField(max_length=70, blank=True)  # 中间件版本
    # todo
    application = models.CharField(max_length=70, blank=True)  # 关联应用系统
    # todo
    cluster = models.CharField(max_length=70, blank=True)  # 关联集群
    HA = models.CharField(max_length=70, blank=True)  # 高可用类型
    create_time = models.CharField(max_length=70, blank=True)  # 安装时间
    jvm_detail = models.CharField(max_length=70, blank=True)  # jvm配制
    jdbc_detail = models.CharField(max_length=70, blank=True)  # jdbc配制

    def __unicode__(self):
        return self.custom_name


##公共平台
class CM_PUBPLATFORM(models.Model):
    id = models.AutoField(primary_key=True)  # 自增主键
    soft_num = models.CharField(max_length=70, blank=True)  # 软件编号
    cluster_name = models.CharField(max_length=70, blank=True)  # 集群名称
    cluster_type = models.CharField(max_length=70, blank=True)  # 集群类型
    cluster_soft = models.CharField(max_length=70, blank=True)  # 集群软件
    soft_version = models.CharField(max_length=70, blank=True)  # 软件版本
    net_local = models.CharField(max_length=70, blank=True)  # 网络位置
    # todo
    server = models.CharField(max_length=70, blank=True)  # 外键关联服务器
    create_time = models.DateField()  # 创建时间

    def __unicode__(self):
        return self.soft_num


# 数据库
class CM_DATABASE(models.Model):
    id = models.AutoField(primary_key=True)  # 自增主键
    pub_platform = models.ForeignKey('CM_PUBPLATFORM')  # 外键关联公共平台
    soft_num = models.CharField(max_length=70, blank=True)  # 软件编号
    custom_name = models.CharField(max_length=70, blank=True)  # 自定义名称
    database_type = models.CharField(max_length=70, blank=True)  # 数据库类型
    database_version = models.CharField(max_length=70, blank=True)  # 数据库版本
    application = models.CharField(max_length=70, blank=True)  # 归属系统
    server = models.CharField(max_length=70, blank=True)  # 安装服务器
    cluster_local = models.CharField(max_length=70, blank=True)  # 所属集群
    database_name = models.CharField(max_length=70, blank=True)  # 数据库名称
    server_ip = models.CharField(max_length=70, blank=True)  # 服务IP
    scan_ip = models.CharField(max_length=70, blank=True)  # 服务器域名
    schema = models.CharField(max_length=70, blank=True)  # schema属性
    create_time = models.DateField()  # 创建时间
    max_session = models.IntegerField()  # 最大会话数
    HA = models.CharField(max_length=70, blank=True)  # 高可用类型
    datasych_type = models.CharField(max_length=70, blank=True)  # 数据同步方式
    data_space = models.IntegerField()  # 表空间

    def __unicode__(self):
        return self.solf_num

class USER_PROFILE(models.Model):
    id = models.AutoField(primary_key=True)
    permission = ( ('read','read'), ('modify','modify'))

class CM_REL_SERVER_MIDWARE(models.Model):
    id = models.AutoField(primary_key=True) #自增主键
    server_id = models.IntegerField() #服务器id
    midware_id = models.IntegerField() #中间件id

class CM_CONFIG(models.Model):
    id = models.AutoField(primary_key=True) #自增主键
    config_name = models.CharField(max_length=70, blank=True)  #配置项名称
    remark = models.CharField(max_length=100, blank=True)  #配置项说明

