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
    print('this is call back function! ', other_param)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # wait方法返回两部分：第一个元素为已完成的Future对象；第二个元素为未完成的部分
    coro = asyncio.wait([outer(1, 2, 3, 4, 5), outer(6, 7, 8, 9, 10)], timeout=5, return_when=asyncio.FIRST_COMPLETED)
    result = loop.run_until_complete(coro)
    print([future.result() for future in result[0]])


