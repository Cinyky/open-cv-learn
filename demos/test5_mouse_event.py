#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 下午4:49
# @Author  : Cyy
# @File    : test5_mouse_event.py
# @Software: PyCharm

import cv2
import numpy as np #mouse callback function
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
    else:
        cv2.rectangle(img, (x,y), (10, 18), (0, 255, 0), 3)
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:
        break
cv2.destroyAllWindows()