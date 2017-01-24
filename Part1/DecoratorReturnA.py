#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps


class Task(object):
    def run(self, *args, **kwargs):
        raise NotImplementedError('Subclasses must implement this method')

    def identify(self):
        return 'i am a task.'


def task(decorated):
    class TaskSubclass(Task):
        def run(self, *args, **kwargs):
            return decorated(*args, **kwargs)

    # 返回Task类的子类
    return TaskSubclass


@task
def foo():
    return 2 + 2


f = foo
print(f)  # <class '__main__.task.<locals>.TaskSubclass'>
print(f())  # 实例 <__main__.task.<locals>.TaskSubclass object at 0x0000003C84E85EF0>
print(f().run())  # 4，看起来着实别扭
