#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)


def test1():
    # 1.绘制一维直方图
    mu = 100
    sigma = 20
    x = mu + sigma * np.random.randn(20000)

    # bins:将20000个数据分成多少份，
    # normed：是否将数据在每一份内统计称概率
    ax.hist(x, bins=200, normed=False)
    plt.show()

def test2():
    # 2.绘制二维直方图
    x = np.random.randn(1000) + 2
    y = np.random.randn(1000) + 3
    ax.hist2d(x, y, bins=40)
    plt.show()

test2()