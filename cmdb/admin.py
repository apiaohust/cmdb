from django.contrib import admin
from cmdb.models import CM_SERVER, CM_OS
admin.site.register(CM_OS)
admin.site.register(CM_SERVER)
