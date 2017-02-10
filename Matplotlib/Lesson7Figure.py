#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10)
# 创建多个画布figure
fig1 = plt.figure()
ax1 = fig1.add_subplot(221)
ax1.plot(x, np.sin(x))

fig2 = plt.figure()
ax2 = fig2.add_subplot(221)
ax2.plot(x, np.cos(x))

plt.show()