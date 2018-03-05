'''
Created on 2018年2月25日

@author: admin
'''
import djcelery
from celery.schedules import crontab
djcelery.setup_loader()
BROKER_URL= 'amqp://guest@localhost//'
# BROKER_URL = 'amqp://root:123456@localhost:5672/demo'
# CELERY_RESULT_BACKEND = 'amqp://guest@localhost//'
# BROKER_URL = 'redis://:dahai123@192.168.5.60:6380/6'
# BROKER_URL = 'redis://:密码@主机地址:端口号/数据库号'

from datetime import timedelta
# celery beat -A  restful  启动定时任务
# celery -A restful worker -l info  启动worker进程

# 一并管理启动，但报错误
# celery -B -A restful worker -l info 
# python manage.py celery worker --loglevel=info --beat
CELERYBEAT_SCHEDULE = {
    'add-every-1-minute': {
        'task': 'demo.tasks.test_multiply',
        # 'schedule': crontab(minute=u'56', hour=u'11',),
        'schedule': crontab(minute='*',hour='*'),
        # 'schedule' : crontab(hour=14, minute=2, day_of_week=2),
        # 'schedule': timedelta(seconds=50),
        'args': (11,10)
    },
    'add-every-3-seconds': {
        'task': 'demo.tasks.test_celery',
        # 'schedule': crontab(minute=u'51', hour=u'11',),
        'schedule': timedelta(seconds=30),
        'args': (16,3)
    },

}

# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'