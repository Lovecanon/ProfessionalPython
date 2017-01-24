#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps
import time


def sorted_by_create_time(cls):
    # 使用sorted_by_create_time方法装饰一个类，实质就是装饰类的__init__方法，
    # 并重写__lt__,__gt__方法
    original_init = cls.__init__  # 保存类的原始方法__init__的副本

    @wraps(original_init)
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self._create_time = time.time()
        time.sleep(1)  # 休眠一秒钟，防止三个实例同一时间创建，

    cls.__init__ = new_init  # 将新的初始化方法赋给cls

    # lambda语句，不需要return，冒号后面就是将要返回的内容
    cls.__lt__ = lambda self, other: self._create_time < other._create_time
    cls.__gt__ = lambda self, other: self._create_time > other._create_time

    return cls


@sorted_by_create_time
class Person(object):
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return self._name

a = Person('A')
b = Person('B')
c = Person('C')
persons = [b, c, a]
print(sorted(persons))



