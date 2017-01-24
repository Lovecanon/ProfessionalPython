#!/usr/bin/env python
# -*- coding: utf-8 -*-


def decorated_by(func):
    print('Decorated bu decorated_by function')
    return func


# 第一种：
def add(x, y):
    """Return the sum of x and y."""
    return x + y


add = decorated_by(add)


# 第二种：注解形式
@decorated_by
def add2(x, y):
    return x + y


if __name__ == '__main__':
    print('execute main()')
    print(add(41, 9))
    print(add2(1, 2))
