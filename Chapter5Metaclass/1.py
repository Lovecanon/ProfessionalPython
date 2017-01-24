#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Hello(object):
    def hello(self, name='world'):
        print('Hello %s.' % name)

h = Hello()
# Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
print(type(Hello))  # <class 'type'>
print(type(h))  # <class '__main__.Hello'>


# type()函数既可以返回一个对象的类型，又可以创建出新的类型
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class
def fn(self, name='World'):
    print('New Hello %s.' % name)
NewHello = type('NewHello', (object,), dict(hello=fn))

nh = NewHello()
print(type(NewHello))  # <class 'type'>
print(type(nh))  # <class '__main__.NewHello'>
nh.hello()







