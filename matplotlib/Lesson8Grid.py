#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.dates as m_date
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
x = np.arange(1, 10, 0.1)


def show_grid():
    # 面向对象的方式显示网格
    ax.plot(x, np.sin(x))
    ax.grid(True, linestyle='--', linewidth=1)
    plt.show()


def show_legend():
    # 显示图例
    ax.plot(x, np.sin(x), label='sin(x)')  # 也可以把label放在ax.legend([.., .., ..])方法中
    ax.plot(x, np.cos(x), label='cos(x)')
    ax.plot(x, np.log(x), label='log(x)')
    # loc：图例的位置，0为自适应；1为右上角；2为左上角
    # ncol：图例按照几列显示，纵向显示不好看可以换成横向显示
    ax.legend(loc=1, ncol=3)
    print(ax.axis([2, 10, 0, 1]))
    plt.show()


def control_axis():
    # 控制坐标轴的长短
    ax.plot(x, np.sin(x), label='sin(x)')
    ax.plot(x, np.cos(x), label='cos(x)')
    ax.plot(x, np.log(x), label='log(x)')
    ax.legend(loc=1, ncol=3)
    ax.axis([2, 10, 0, 1])  # 控制纵横坐标轴的大小，传入x轴的左右边界和y轴
    plt.show()


def control_axis_locator():
    # 控制坐标轴刻度显示
    ax.plot(x, np.sin(x), label='sin(x)')
    ax.legend(loc=1)
    ax.locator_params('y', nbins=10)  # 将y轴的刻度分成20份
    plt.show()


def control_axis_date():
    stock_date, open_price = np.loadtxt('./data/2.csv', delimiter=',', converters={0: m_date.bytespdate2num('%Y-%m-%d')}, skiprows=1,
               usecols=(0, 1), unpack=True)
    ax.plot_date(stock_date, open_price, linestyle='-', marker='')
    date_formatter = m_date.DateFormatter('%Y/%m')
    ax.xaxis.set_major_formatter(date_formatter)  # 设置x轴的格式
    fig.autofmt_xdate()  # x轴日期太长就给他倾斜表现
    plt.show()


def add_axis():
    # 增加一个y轴
    y1 = x * x
    y2 = np.log(x)
    ax.plot(x, y1)
    ax.set_ylabel('Y1')

    ax2 = ax.twinx()
    ax2.plot(x, y2)
    ax2.set_ylabel('Y2')

    ax.set_xlabel('use common x axis')
    plt.show()


if __name__ == '__main__':
    add_axis()
