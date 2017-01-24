#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ContextManager(object):
    def __init__(self):
        self.entered = False

    def __enter__(self):
        self.entered = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.entered = False

cm = ContextManager()
print(cm.entered)  # False只是创建一个ContextManager实例，entered属性仍然为False

# with执行后面的语句，并返回__enter__方法返回的东西，这里是self,即：ContextManager实例
with ContextManager() as c:
    print(c.entered)  # True






