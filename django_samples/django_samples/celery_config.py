# -*- coding: utf-8 -*-
# @Time : 2023/3/25 22:13
# @Author : hehaiyang
# @File : celery.py
# @Project : django_samples
# @Function :
from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_samples.settings')

app = Celery('django_samples')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
# from django_celery_beat.models import IntervalSchedule

app.conf.beat_schedule = {
    # 定时任务
    'add-every-day-at-08-40': {
        'task': 'apps.chatgpt.tasks.add_1',
        'schedule': crontab(minute='40', hour='08'),
        'args': (16, 16),
    },
    'mul-every-day-at-08-40': {
        'task': 'apps.chatgpt.tasks.mul',
        'schedule': crontab(minute='40', hour='08'),
        'args': (16, 16),
    },
    # 周期任务
    'add-every-5-seconds': {
        'task': 'apps.chatgpt.tasks.add_1',
        'schedule': 5.0,
        'args': (16, 16),
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
