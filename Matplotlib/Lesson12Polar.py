#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Matplotlib.pyplot as plt
import numpy as np


def polar():
    # 绘制极坐标图像
    r = np.arange(1, 6, 1)
    theta = np.arange(0, 2.1, 0.5) * np.pi
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='polar')
    ax.plot(theta, r, color='r', linewidth=1)
    ax.grid(True)
    plt.show()

    # r = np.empty(5).fill(5)  # 生成一个长度为5的且用元素5来填充的数组


if __name__ == '__main__':
    polar()