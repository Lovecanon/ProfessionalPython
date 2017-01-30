#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
x = np.linspace(0, 5 * np.pi, 1000)


def fill():
    # 曲线填充
    y1 = np.sin(x)
    y2 = np.sin(2 * x)
    # ax.plot(x, y1)  # 既然是填充，没必要画出曲线勒
    # ax.plot(x, y2)
    ax.fill(x, y1, 'b', alpha=0.3)
    ax.fill(x, y2, 'r', alpha=0.3)
    plt.show()


def fill_between():
    # 曲线填充，如果y1在y2曲线下面用yellow颜色填充；如果y1在y2曲线上面用green颜色填充。
    y1 = np.sin(x)
    y2 = np.sin(2 * x)
    ax.plot(x, y1, 'b')
    ax.plot(x, y2, 'r')
    ax.fill_between(x, y1, y2, where=y1 <= y2, facecolors='yellow', alpha=0.5)
    ax.fill_between(x, y1, y2, where=y1 > y2, facecolors='green', alpha=0.5)
    plt.show()


def patch():
    # 在坐标轴上画各种小图形，x和y坐标轴的长短根据小图形来定
    circle = patches.Circle([2, 2], 1)  # 圆形
    ax.add_patch(circle)

    rect = patches.Rectangle([2, 8], 1, 2, color='r')  # 长方形
    ax.add_patch(rect)

    regu = patches.RegularPolygon([8, 2], 5, 2, color='r')  # 多边形，这里是五边形，长度为2
    ax.add_patch(regu)

    ax.axis('equal')  # 使x，y坐标轴比例为1。等价于：plt.axes(aspect=1)
    plt.show()


if __name__ == '__main__':
    patch()
