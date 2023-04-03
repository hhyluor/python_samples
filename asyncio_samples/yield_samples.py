# -*- coding: utf-8 -*-
# @Time : 2023/3/23 14:54
# @Author : hehaiyang
# @File : yield_samples.py
# @Project : python_samples
# @Function :
def func1():
    yield 1
    yield from func2()
    yield 2


def func2():
    yield 3
    yield 4


f1 = func1()
for item in f1:
    print(item)