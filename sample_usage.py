#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:32:46 2021

@author: ahmet
"""

import cv2
import numpy as np
import auto_canny as ac

camera=cv2.VideoCapture(0) #webcamm açmak için 0 yazdık. Video dosya yolu da girilebilir

while True:
    ret,image=camera.read()
    img_blur=cv2.blur(image,(2,2)) #gürültü azaltmak için
    edges = ac.canny_smart(img_blur,0.33)
    cv2.imshow("edges",edges)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
camera.release()
cv2.destroyAllWindows()
