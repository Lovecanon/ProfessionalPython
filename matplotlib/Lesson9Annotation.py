#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111)
x = np.arange(-5, 5, 0.1)

def annotation():
    ax.plot(x, x**2)
    # xy：表示要标注的坐标
    # xytext：注解文字的坐标
    # arrowprops：箭头个各个属性设置
    # headlength：箭头的箭的长度
    # width：箭神的宽度
    ax.annotate('this is annotation', xy=(0, 0), xytext=(1, 4),
                arrowprops=dict(facecolor='c', headlength=16, headwidth=8, width=4))
    plt.show()


def font():
    ax.plot(x, x**2)
    # 在(-0.5, 10)坐标点添加一段文字，并控制字体样式和字体边框bbox样式
    ax.text(-.5, 10, 'this is y=x^2', family='serif', size=10, color='r', style='italic', weight='black')
    ax.text(-.5, 5, 'this is y=x^2', family='serif', size=10, color='c', style='italic', weight='light',
            bbox=dict(facecolor='red', alpha=0.5))
    plt.show()

def teX():
    # 数学公式的写法
    ax.set_xlim([1, 7])
    ax.set_ylim([1, 5])
    # r：表示不转义
    ax.text(2, 4, r'$ \alpha_i \beta_j \pi \lambda \omega $', size=15)
    plt.show()





if __name__ == '__main__':
    teX()