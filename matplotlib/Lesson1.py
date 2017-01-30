#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

s_open, s_close = np.loadtxt('./data/1.csv', skiprows=1, usecols=(1, 4), delimiter=',', unpack=True)
change = s_close - s_open
yesterday = change[:-1]
today = change[1:]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(yesterday, today, s=10, marker='s', c='g')
plt.show()