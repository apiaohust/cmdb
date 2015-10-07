# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CM_APP',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('apply_num', models.CharField(max_length=70, blank=True)),
                ('base_info', models.CharField(max_length=100, blank=True)),
                ('system_status', models.CharField(max_length=70, blank=True)),
                ('dev_strategy', models.CharField(max_length=70, blank=True)),
                ('first_field', models.CharField(max_length=70, blank=True)),
                ('second_field', models.CharField(max_length=70, blank=True)),
                ('tech_depart', models.CharField(max_length=70, blank=True)),
                ('app_admin', models.CharField(max_length=70, blank=True)),
                ('yw_depart', models.CharField(max_length=70, blank=True)),
                ('yw_admin', models.CharField(max_length=70, blank=True)),
                ('op_level', models.CharField(max_length=70, blank=True)),
                ('server_time', models.CharField(max_length=70, blank=True)),
                ('zaibei_status', models.CharField(max_length=70, blank=True)),
                ('is_opensource', models.CharField(max_length=70, blank=True)),
                ('RTO', models.CharField(max_length=70, blank=True)),
                ('RPO', models.CharField(max_length=70, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CM_CONFIG',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('config_name', models.CharField(max_length=70, blank=True)),
                ('remark', models.CharField(max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CM_DATABASE',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('soft_num', models.CharField(max_length=70, blank=True)),
                ('custom_name', models.CharField(max_length=70, blank=True)),
                ('database_type', models.CharField(max_length=70, blank=True)),
                ('database_version', models.CharField(max_length=70, blank=True)),
                ('application', models.CharField(max_length=70, blank=True)),
                ('server', models.CharField(max_length=70, blank=True)),
                ('cluster_local', models.CharField(max_length=70, blank=True)),
                ('database_name', models.CharField(max_length=70, blank=True)),
                ('server_ip', models.CharField(max_length=70, blank=True)),
                ('scan_ip', models.CharField(max_length=70, blank=True)),
                ('schema', models.CharField(max_length=70, blank=True)),
                ('create_time', models.DateField()),
                ('max_session', models.IntegerField()),
                ('HA', models.CharField(max_length=70, blank=True)),
                ('datasych_type', models.CharField(max_length=70, blank=True)),
                ('data_space', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CM_MIDWARE',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('solf_num', models.CharField(max_length=70, blank=True)),
                ('custom_name', models.CharField(max_length=70, blank=True)),
                ('mid_type', models.CharField(max_length=70, blank=True)),
                ('mid_name', models.CharField(max_length=70, blank=True)),
                ('mid_version', models.CharField(max_length=70, blank=True)),
                ('application', models.CharField(max_length=70, blank=True)),
                ('cluster', models.CharField(max_length=70, blank=True)),
                ('HA', models.CharField(max_length=70, blank=True)),
                ('create_time', models.CharField(max_length=70, blank=True)),
                ('jvm_detail', models.CharField(max_length=70, blank=True)),
                ('jdbc_detail', models.CharField(max_length=70, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CM_OS',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('number', models.CharField(max_length=50, blank=True)),
                ('type', models.CharField(max_length=50, blank=True)),
                ('version', models.CharField(max_length=50, blank=True)),
                ('create_time', models.DateField()),
                ('disk_content', models.IntegerField()),
                ('memory', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CM_PUBPLATFORM',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('soft_num', models.CharField(max_length=70, blank=True)),
                ('cluster_name', models.CharField(max_length=70, blank=True)),
                ('cluster_type', models.CharField(max_length=70, blank=True)),
                ('cluster_soft', models.CharField(max_length=70, blank=True)),
                ('soft_version', models.CharField(max_length=70, blank=True)),
                ('net_local', models.CharField(max_length=70, blank=True)),
                ('server', models.CharField(max_length=70, blank=True)),
                ('create_time', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CM_REL_SERVER_MIDWARE',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('server_id', models.IntegerField()),
                ('midware_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CM_SERVER',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('hardware_num', models.CharField(max_length=50, blank=True)),
                ('architecture', models.CharField(max_length=50, blank=True)),
                ('version', models.CharField(max_length=50, blank=True)),
                ('cpu_count', models.IntegerField()),
                ('memory', models.IntegerField()),
                ('detail', models.CharField(max_length=700, blank=True)),
                ('fun_name', models.CharField(max_length=100, blank=True)),
                ('admin_ip', models.CharField(max_length=100, blank=True)),
                ('server_ip', models.CharField(max_length=100, blank=True)),
                ('net_local', models.CharField(max_length=50, blank=True)),
                ('vcluster', models.IntegerField()),
                ('m_room', models.CharField(max_length=70, blank=True)),
                ('m_cabinet', models.CharField(max_length=50, blank=True)),
                ('m_cabloc', models.CharField(max_length=50, blank=True)),
                ('buy_time', models.DateField()),
                ('set_time', models.DateField()),
                ('monitor', models.CharField(max_length=100, blank=True)),
                ('datebase', models.IntegerField()),
                ('midleware', models.IntegerField()),
                ('HA', models.CharField(max_length=50, blank=True)),
                ('status', models.CharField(max_length=50, blank=True)),
                ('ex_store', models.CharField(max_length=50, blank=True)),
                ('ex_miya', models.CharField(max_length=50, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CM_VCLUSTER',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('hard_num', models.CharField(max_length=70, blank=True)),
                ('cluster_name', models.CharField(max_length=70, blank=True)),
                ('cluster_type', models.CharField(max_length=70, blank=True)),
                ('cluster_solft', models.CharField(max_length=70, blank=True)),
                ('soft_version', models.CharField(max_length=70, blank=True)),
                ('net_local', models.CharField(max_length=70, blank=True)),
                ('server', models.CharField(max_length=70, blank=True)),
                ('create_time', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='USER_PROFILE',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('permission', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cm_os',
            name='server',
            field=models.ForeignKey(to='cmdb.CM_SERVER'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cm_midware',
            name='pub_platform',
            field=models.ForeignKey(to='cmdb.CM_PUBPLATFORM'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cm_midware',
            name='server',
            field=models.ForeignKey(to='cmdb.CM_SERVER'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cm_database',
            name='pub_platform',
            field=models.ForeignKey(to='cmdb.CM_PUBPLATFORM'),
            preserve_default=True,
        ),
    ]
