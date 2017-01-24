#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from functools import wraps


def json_output(decorated):
    @wraps(decorated)
    def inner(*args, **kwargs):
        name, age = decorated(*args, **kwargs)
        return json.dumps({'name': name, 'age': age})

    return inner


class Person(object):
    def __init__(self, name):
        self._name = name

    @json_output
    def show_person(self, age=20):
        return self._name, age

j = Person('Jack').show_person(23)
print(j)