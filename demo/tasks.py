'''
Created on 2018年1月31日

@author: '卓小建'
'''
from __future__ import absolute_import

import logging
from celery import task
from celery.utils.log import get_task_logger

import time
import http.client
import json
@task
def test_celery(x, y):
    logger = get_task_logger(__name__)
    logger.info("========================test_celery===========================")
    logger.info('func start  ----------------->')
    logger.info('application:%s', "test_celery")
    logger.info('func end -------------------->')
    print('本次结果为：',x + y)
    return x + y


@task
def test_multiply(x, y):
    logger = get_task_logger(__name__)
    logger.info("========================test_multiply===========================")
   
    logger.info('func start  ----------------->')
    logger.info('application:%s', "test_multiply")
    logger.info('func end -------------------->')
    print('本次结果为：',x * y)
    return x * y

'''
模拟长时间计算
'''
@task
def test_add(x, y):
    logger = get_task_logger(__name__)
    logger.info("=========================开始计算======================================")
    logger.info('本次结果为：', x+y)
    logger.info("===========================异步完成=============================================")
    time.sleep(10)
    return x + y



@task
def http_get_request():
    logger = get_task_logger(__name__)
    logger.info("=====================开始异步request请求==========================")
    request_url = "https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=2&max_behot_time=0&max_behot_time_tmp=1514009093&tadrequire=true&as=A1359A63AD0FE1C&cp=5A3DDF9EA1DC5E1&_signature=H0ueLAAARXrRIBj-OHrK7h9Lnj"
    conn = http.client.HTTPSConnection('www.toutiao.com')
    conn.request(method="POST", url=request_url)
    response = conn.getresponse()
    res = response.read()
    str = res.decode("unicode-escape")
    logger.info(str)
    json_string = json.dumps(str)
    python_obj = json.loads(json_string)
    logger.info("python_obj:" , python_obj)
    logger.info("=======================结束异步request请求========================")



