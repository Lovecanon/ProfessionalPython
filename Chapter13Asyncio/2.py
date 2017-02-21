import asyncio
from functools import partial


@asyncio.coroutine
def nested(*args):
    print('the nested() function is ran with args: %r' % (args,))
    return [i + 1 for i in args]


@asyncio.coroutine
def outer(*args):
    print('the outer() function is ran with args: %r' % (args,))
    answer = yield from nested(*[i ** 2 for i in args])
    return answer


def callback_func(other_param, feature):
    # 任务(task)的回调函数为普通函数，但必须只有一个feature参数。
    # 如果需要其他参数使用偏函数传给add_done_callback
    print('this is call back function! ', other_param)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # 1.直接传递一个函数对象给事件循环，coroutine注解使函数返回一个generator对象
    # r = loop.run_until_complete(outer(1, 2, 3, 4, 5))
    # print(r)

    # 2.Task是Future的子类，之前向run_until_complete函数传递一个协程时，该协程会被包装到一个Task对象中并执行
    # Task对象的任务：
    # a.存储结果并为yield from语句提供值
    # b.能够将回调注册到Future。回调就是在Future完成后执行的一个函数，该函数接受Future作为参数
    task = asyncio.ensure_future(outer(1, 2, 3, 4, 5))  # 将协程放入事件循环并返回对应的Task对象
    task.add_done_callback(partial(callback_func, 'thx'))
    loop.run_forever()

    print('task status:%s, result:%s' % (task.done(), task.result()))

