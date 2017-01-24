#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps


class Task(object):
    # Python中有一个有趣的语法，只要定义类型的时候，实现__call__函数，这个类型就成为可调用的。
    # 我们可以把这个类的对象当作函数来使用，相当于重载了括号运算符。
    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def run(self, *args, **kwargs):
        raise NotImplementedError('Subclasses must implement this method')

    def identify(self):
        return 'i am a task.'


def task(decorated):
    class TaskSubclass(Task):
        def run(self, *args, **kwargs):
            return decorated(*args, **kwargs)

    # 返回Task类的子类
    return TaskSubclass()


@task
def foo():
    return 2 + 2


f = foo
print(f)  # 直接返回类的实例 <__main__.task.<locals>.TaskSubclass object at 0x0000002A7A595EF0>
print(f())  # 因为定义了__call__方法，该实例f即为可调用的，即执行定义的__call__方法
