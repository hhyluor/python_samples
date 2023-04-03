# -*- coding: utf-8 -*-
# @Time : 2023/3/4 20:49
# @Author : hehaiyang
# @File : tasks.py
# @Project : django_samples
# @Function :
from celery import shared_task

@shared_task
def add(x, y):
    return x + y
