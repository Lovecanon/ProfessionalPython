#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password


class AnonymousUser(User):
    def __init__(self):
        super().__init__(None, None)

    # Python中默认将所有的空对象定义为布尔意义上的False,
    # 在自己定义的类中我们也可以加入自定义的布尔判断标准,这里始终返回False
    def __bool__(self):
        return False


def require_user(decorated):
    @wraps(decorated)
    def inner(user, *args, **kwargs):
        # 如果用户是Anonymous，__bool__无路如何都会返回False
        if user and isinstance(user, User):
            return decorated(user, *args, **kwargs)
        else:
            raise ValueError('A valid user is required to visit this method!')

    return inner


@require_user
def update_info(user):
    print('Success update user info.')


# update_info(User('a', 'b'))

update_info(AnonymousUser())
