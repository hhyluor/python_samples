# -*- coding: utf-8 -*-
# @Time : 2023/3/23 14:52
# @Author : hehaiyang
# @File : greenlet_samples.py
# @Project : python_samples
# @Function :
from greenlet import greenlet


def func1():
    print(1)        # 第1步：输出 1
    gr2.switch()    # 第3步：切换到 func2 函数
    print(2)        # 第6步：输出 2
    gr2.switch()    # 第7步：切换到 func2 函数，从上一次执行的位置继续向后执行


def func2():
    print(3)        # 第4步：输出 3
    gr1.switch()    # 第5步：切换到 func1 函数，从上一次执行的位置继续向后执行
    print(4)        # 第8步：输出 4


gr1 = greenlet(func1)
gr2 = greenlet(func2)

gr1.switch() # 第1步：去执行 func1 函数