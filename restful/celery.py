'''
Created on 2018年1月31日

@author: admin
'''

from __future__ import absolute_import

import os

from celery import Celery, platforms

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restful.settings')

from django.conf import settings  # noqa

app = Celery('restful')
platforms.C_FORCE_ROOT = True

# Using a string here means the worker will not have to
# pickle the object when using Windows.
# app.config_from_object('django.conf:settings')
app.config_from_object('restful.config')    #以config.py作为配置文件导入参数
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print("====================debug_task=============================")
    print('Request: {0!r}'.format(self.request))

