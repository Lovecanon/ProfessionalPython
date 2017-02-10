#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


def test1():
    # 一.绘制一般的条形图
    fig = plt.figure()
    ax = fig.add_subplot(111)
    y = [20, 10, 30, 15, 10]  # 有五个数据，
    x = range(5)
    # ax.bar(left=x, height=y, width=0.35)

    # 2.绘制向右的条形图
    ax.bar(left=0, bottom=x, height=0.5, width=y, orientation='horizontal')

    plt.show()


def test2():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    sales_BJ = [20, 10, 30, 15, 10]
    sales_SH = [40, 20, 10, 10, 20]
    x = np.arange(5)
    bar_width = 0.35
    ax.bar(x, sales_BJ, bar_width)
    # 1.并列显示
    # ax.bar(x + bar_width, sales_SH, bar_width)

    # 2.层叠显示
    ax.bar(x, sales_BJ, bar_width, bottom=sales_BJ)
    plt.show()

test1()