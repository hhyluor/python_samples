# -*- coding: utf-8 -*-
# @Time : 2023/3/25 22:52
# @Author : hehaiyang
# @File : tasks.py
# @Project : django_samples
# @Function :
# Create your tasks here

from celery import shared_task


@shared_task
def add_1(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


