#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MyClass(object):
    def __new__(cls, *args, **kwargs):
        # 1.__new__在__init__方法之前执行，用于创建类的实例并返回该实例，
        # __init__方法负责在实例创建后对其进行自定义。
        # 2.cls参数是创建实例所需要的类，
        # __new__方法的其他参数会被完整的复制到__init__方法中。
        # 参数在调用类构造函数时首先会被传递给__new__方法，然后传递给 __init__方法
        # 3.只有通过__new__方法返回当前类的实例时才会执行__init__方法
        print('__new__() execute.', args, kwargs)

        return super(MyClass, cls).__new__(cls,)

    def __init__(self, count, **kwargs):
        print('__init__() execute.')

    def __eq__(self, other):
        return type(self) == type(other)

    def __str__(self):
        # 当对象被传递给接收str类型的参数时调用该方法
        return 'myClass'

    def __repr__(self):
        # 用于确定该对象在python交互式终端中的显示方式
        return '<myClass>'


if __name__ == '__main__':
    m = MyClass(10, num=20)

    # __new__()  execute.(10, ) {'num': 20}
    # __init__() execute.
    # myClass
