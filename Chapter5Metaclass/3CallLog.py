#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CallLogged(type):
    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            # key为函数名，value为函数对象
            if callable(value):
                # 使用装饰器
                attrs[key] = cls.log_call(value)
        return super(CallLogged, cls).__new__(cls, name, bases, attrs)

    @staticmethod
    def log_call(fxn):
        def inner(*args, **kwargs):
            print('call %s method, with arguments is %r、%r' % (fxn.__name__, args, kwargs))
            try:
                response = fxn(*args, **kwargs)
                print('call %s method successfully.' % (fxn.__name__,))
                return response
            except Exception as e:
                print('call %s method and raised an exception:%r' % (fxn.__name__, e))
                raise  # 将错误抛给调用者
        return inner


class MyClass(metaclass=CallLogged):
    # 没有显示的写出__init__方法在实例化对象时不会记录object类中对__init__方法的调用
    name = 'L'
    def foo(self):
        print('foo()')

    def bar(self):
        raise TypeError('oh noes!')

if __name__ == '__main__':
    m = MyClass()
    print(m.name)












