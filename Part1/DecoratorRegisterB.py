#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Registry(object):
    def __init__(self):
        self._functions = []

    def register(self, decorated):
        self._functions.append(decorated)
        return decorated

    # *args表示可接受任意数量的位置参数,args是一个元组
    # **kwargs表示可接受任意数量的关键字参数，kwargs是一个dict
    # *args,**kwargs必须放在函数的参数最后位置
    # 接受关键字参数的函数：
    # 1.run_all(self, *args，name='admin')放在接受任意参数的位置参数后；
    # 2. run_all(self, *, name)或用星号隔开
    def run_all(self, *args, **kwargs):
        return_value = []
        for func in self._functions:
            return_value.append(func(*args, **kwargs))
        return return_value


a = Registry()
b = Registry()


@a.register
def foo(x=3):
    return x


@b.register
def bar(x=5):
    return x


@b.register
@a.register
def baf(x=7):
    return x


# 两个不同的注册表实例，可以拥有完全分离的注册表。甚至可以使用多个注册表注册同一函数baf。
print(a.run_all())
print(b.run_all())
# run_all()方法能够接受参数，运行时将参数传入底层函数
print(a.run_all(4))
