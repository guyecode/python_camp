# coding: utf-8
import math
import time
import functools


def timeit1(func):
    """打印函数的执行时间"""
    def calc_time(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print('cost %s seconds' % (time.time() - start))
        return result
    return calc_time


def timeit2(func):
    """功能和timeit1一样，只是加用wraps方法包装了一下"""
    @functools.wraps(func)
    def calc_time(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print('cost %s seconds' % (time.time() - start))
        return result
    return calc_time



@timeit1
def f1(x=10000):
    """hahaha"""
    for i in range(x):
        math.sqrt(i)
f1()
# 打印出来的实际是calc_time的名称和文档
print(f1.__name__)
print(f1.__doc__)

@timeit2
def f2(x=10000):
    """hahaha"""
    for i in range(x):
        math.sqrt(i)
f2()
# 打出出来的是f2自己的名称和文档
print(f2.__name__)
print(f2.__doc__)