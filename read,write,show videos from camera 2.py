# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#print("Hello, Worldd!")
'''import numpy as np
import matplotlib.pyplot as plt
import pandas as pd'''

import cv2
cap = cv2.VideoCapture(0)
while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()    
