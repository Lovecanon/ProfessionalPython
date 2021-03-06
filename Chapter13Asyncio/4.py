# clone from github TensorFlow-and-DeepLearning-Tutorial project
import socket  # on top of TCP
import time
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

# select: System Call -----> watch the readiness of a unix-file(socket) i/o
# only socket is possible in Windows
# non-blocking socket


selector = DefaultSelector()


class Future:  # ~=Promise, return the caller scope a promise
    # about something in the future
    def __init__(self):
        self.callbacks = []

    def resolve(self):  # on future event callback
        for func in self.callbacks:
            func()


class Task:  # responsible for calling next() on generators
    # in charge of the async functions
    def __init__(self, gen, eventLoop):
        self.gen = gen
        self.step()

    def step(self):  # go to next step/next yield
        try:
            f = next(self.gen)
            f.callbacks.append(self.step)
        except StopIteration as e:
            # Task is finished
            eventLoop.n_task -= 1


class EventLoop:
    def __init__(self):
        self.n_task = 0

    def add_task(self, generator):
        self.n_task += 1
        Task(generator, self)

    def start(self):
        while self.n_task > 0:
            events = selector.select()
            for event, mask in events:
                f = event.data
                f.resolve()


def pause(s, event):
    f = Future()
    selector.register(s.fileno(), event, data=f)
    yield f  # pause this function


def resume(s):
    selector.unregister(s.fileno())


def async_await(s, event):
    yield from pause(s, event)
    resume(s)


def async_get(path):
    s = socket.socket()
    s.setblocking(False)
    try:
        s.connect(('127.0.0.1', 8000))
    except BlockingIOError as e:
        print(e)

    yield from async_await(s, EVENT_WRITE)

    request = 'GET %s HTTP/1.0\r\n\r\n' % path
    s.send(request.encode())

    totalReceived = []
    while True:
        yield from async_await(s, EVENT_READ)

        received = s.recv(1024)
        if received:
            totalReceived.append(received)
        else:
            body = (b''.join(totalReceived)).decode()
            print('--------------------------------------')
            print(body.split('\r\n\r\n')[0])
            print('--------------------------------------', 'Byte Received:', len(body), '\n\n')
            return


if __name__ == '__main__':
    start = time.time()
    eventLoop = EventLoop()

    for i in range(50):
        eventLoop.add_task(async_get('/blog/'))

    eventLoop.start()

    print('%.1f sec' % (time.time() - start))
