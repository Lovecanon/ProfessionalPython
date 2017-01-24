#!/usr/bin/env python
# -*- coding: utf-8 -*-

registry = []


def register(decorated):
    registry.append(decorated)
    return decorated


@register
def foo():
    return 1


@register
def bar():
    return 2


answer = []
for func in registry:
    answer.append(func())

print(answer)
