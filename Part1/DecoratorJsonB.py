#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps
import json


class JSONOutputError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


def json_output(indent=None, sort_key=False):
    def actual_decorator(decorated):
        @wraps(decorated)
        def inner(*args, **kwargs):
            try:
                result = decorated(*args, **kwargs)
            except JSONOutputError as ex:
                result = {
                    'status': 'Error',
                    'message': str(ex)
                }
            return json.dumps(result, indent=indent, sort_keys=sort_key)

        return inner

    return actual_decorator


@json_output(indent=4)
def do_nothing():
    return {'Person': 'Jack'}

r = do_nothing()
print(r)