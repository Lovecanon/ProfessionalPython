#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

print(plt.style.available)  # 打印出可以使用的样式
plt.style.use('ggplot')  # 使用ggplot样式

fig, axs = plt.subplots(ncols=2, nrows=2)
ax1, ax2, ax3, ax4 = axs.ravel()

# 1.绘制一个散点图
x, y = np.random.normal(size=(2, 50))
ax1.scatter(x, y, s=5)

# 2.绘制一个条形图
x = np.arange(0, 10)
y = np.arange(0, 10)
n_colors = len(plt.rcParams['axes.prop_cycle'])
interval = np.linspace(0, 10, n_colors)
for i in interval:
    ax2.plot(x, y + i, '-')

# 3.绘制并列直方图
x = np.arange(0, 10)
y1, y2, y3 = np.random.randint(0, 20, size=(3, 10))
bar_width = 0.2
ax3.bar(x, y1, bar_width, color='green')
ax3.bar(x + bar_width, y2, bar_width, color='blue')
ax3.bar(x + 2 * bar_width, y3, bar_width, color='cyan')

# 4.绘制小图像放入坐标轴中
circle_centre = np.random.randint(1, 10, size=(n_colors, 2))
for i, color in enumerate(plt.rcParams['axes.prop_cycle']):
    # 因为plt.rcParams['axes.prop_cycle']返回的是一个dict类型数据，故需要使用color['color']
    ax4.add_patch(patches.Circle(circle_centre[i], radius=.5, color=color['color']))

ax4.axis('equal')

plt.show()
