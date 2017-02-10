#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np

# 因为都出文件后以bytes形式存储在内存中，dates.strpdate2num报错就换成dates.bytespdate2num方法。
date, open_price, close_price = np.loadtxt('./data/2.csv', delimiter=',', converters={0: dates.bytespdate2num('%Y-%m-%d')},
                                           usecols=(0, 1, 4), unpack=True, skiprows=1)

fig = plt.figure()
ax = fig.add_subplot(111)
# ax.plot(date, open_price)  # 这种方法横轴是日期的表现浮点数
# plot_date直接绘制带日期的坐标轴，默认绘制散点图，添加linestyle='-'可变为折线图
ax.plot_date(date, open_price, linestyle='-', color='green', marker='o', markersize=2)
plt.show()
