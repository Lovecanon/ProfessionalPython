#!/usr/bin/env python
# -*- coding: utf-8 -*-
# metaclass
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。


class ListMetaclass(type):
    # __new__方法参数：当前准备创建的类的对象；类的名字；类继承的父类集合；类的方法集合。
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass

l = MyList()
l.add('d')
print(l)



