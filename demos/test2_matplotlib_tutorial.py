#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 上午10:44
# @Author  : Cyy
# @File    : test2_matplotlib_tutorial.py
# @Software: PyCharm

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../images/timg.jpeg',0)
plt.imshow(img, cmap = 'Blues', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()