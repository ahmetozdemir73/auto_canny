#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 21:41:05 2021

@author: ahmet
"""

import cv2
import numpy as np


def canny_smart(img,sigma=0.33):
	#görüntüdeki piksel yoğunluklarının medyanı hesaplanır
	v = np.median(img)
	# canny ile kenar tespiti için alt ve üst threshold değerleri ortama göre otomatik olarak hesaplanır
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
    # hesaplanan threshold değerleri kullanılarak görüntüye Canny algoritması uygulanır
	edged = cv2.Canny(img, lower, upper)

	return edged

