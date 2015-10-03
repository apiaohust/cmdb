# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cm_server',
            old_name='server',
            new_name='pub_platform',
        ),
        migrations.AlterField(
            model_name='cm_server',
            name='detail',
            field=models.CharField(max_length=700, blank=True),
            preserve_default=True,
        ),
    ]
