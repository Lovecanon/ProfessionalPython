#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps


def require_ints(decorated):
    # @ wraps(decorated)  # 如果想让help(add)返回add的函数对象，就必须添加这个注解，实质上还是调用inner方法。
    def inner(*args, **kwargs):
        for value in args + tuple(kwargs.values()):
            if not isinstance(value, int):
                raise TypeError('%s method only accept integers as arguments!' % (decorated.__name__,))
        return decorated(*args, **kwargs)  # 执行decorated方法，并返回结果

    return inner


@require_ints
def add(x, y):
    return x + y

# 返回inner(*args, **kwargs)的函数对象
# 此时：inner函数没有被调用。
help(add)
# 此时：调用add(3, 5)即调用inner(3, 5),inner函数执行类型检查并返回decorated(*args, **kwargs)执行结果
result = add(3, 5)
print(result)
