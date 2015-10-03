__author__ = 'lenovo'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pythonPro.settings')

import cmdb
cmdb.setup()

from cmdb.models import CM_OS, CM_SERVER
