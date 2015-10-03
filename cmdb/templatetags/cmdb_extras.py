__author__ = 'lenovo'
from django import template
from cmdb.models import CM_SERVER

register = template.Library()

@register.inclusion_tag('cmdb/serverlist.html')

def get_server_list():
    return {'serverlist':CM_SERVER.objects.all()}