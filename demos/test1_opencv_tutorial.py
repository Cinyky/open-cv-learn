#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 上午10:27
# @Author  : Cyy
# @File    : test1_opencv_tutorial.py
# @Software: PyCharm

import cv2

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img = cv2.imread("../images/timg.jpeg")
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k==27: #waitforESCkeytoexit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('../images/copy.png', img)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows