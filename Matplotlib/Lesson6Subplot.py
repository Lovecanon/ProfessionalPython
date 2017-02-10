#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10)
# 创建多个子图subplot
fig = plt.figure(figsize=(10, 4))

# subplot(numRows, numCols, plotNum)
# subplot将整个绘图区域等分为numRows行 * numCols列个子区域，然后按照从左到右，从上到下的顺序对每个子区域进行编号，
# 左上的子区域的编号为1。
ax1 = fig.add_subplot(221)  # 第一行的左图
ax1.plot(x, np.sin(x))

ax2 = fig.add_subplot(222)  # 第一行的右图
ax2.plot(x, np.cos(x))
ax3 = fig.add_subplot(212)  # 第二整行
ax3.plot(x, np.tan(x))

plt.show()
