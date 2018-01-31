'''
Created on 2018年1月31日

@author: '卓小建'
'''
from __future__ import absolute_import

import logging
from celery import task
from celery.utils.log import get_task_logger
from celery.schedules import crontab


@task
def test_celery(x, y):
    logger = get_task_logger(__name__)
    logger.info("========================test_celery===========================")
    logger.info('func start  ----------------->')
    logger.info('application:%s', "TEST_APP")
    logger.info('func end -------------------->')
    print(x + y)
    return x + y


@task
def test_multiply(x, y):
    logger = get_task_logger(__name__)
    logger.info("========================test_celery===========================")
   
    logger.info('func start  ----------------->')
    logger.info('application:%s', "TEST_APP")
    logger.info('func end -------------------->')
    print(x * y)
    return x * y