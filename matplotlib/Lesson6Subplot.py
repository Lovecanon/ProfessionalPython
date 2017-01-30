#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10)
# 创建多个子图subplot
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.plot(x, np.sin(x))

ax2 = fig.add_subplot(222)
ax2.plot(x, np.cos(x))
ax3 = fig.add_subplot(223, )

plt.show()