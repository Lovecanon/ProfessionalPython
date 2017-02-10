#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

plt.axes(aspect=1)  # 横轴和纵轴比例为1:1

labels = ['A', 'B', 'C', 'D']
fracs = [15, 30, 45, 10]
explode = [0, 0.2, 0, 0]  # 突出显示第二个部分
plt.pie(x=fracs, labels=labels, autopct='%.00f%%', explode=explode)
plt.show()
