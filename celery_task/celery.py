#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffyapi.settings.dev')
django.setup()

from celery import Celery

broker = 'redis://127.0.0.1:6379/11'
backend = 'redis://127.0.0.1:6379/12'
include = ['celery_task.tasks', ]
app = Celery(broker=broker, backend=backend, include=include)

# 自动添加任务
# 时区
app.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
app.conf.enable_utc = False

# 任务的定时配置
from datetime import timedelta
from celery.schedules import crontab
app.conf.beat_schedule = {
    'django-task': {
        'task': 'celery_task.tasks.django_task',
        'schedule': timedelta(seconds=60 * 60),
        # 'schedule': crontab(hour=8, day_of_week=1),  # 每周一早八点
        'args': (),
    },
}

# 启动 添加任务 服务的命令
# celery worker -A celery_task -l info -P eventlet

