# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:10:28 2019

@author: Owner
"""

import cv2
import numpy as np

img = np.zeros((512,512,3))
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()