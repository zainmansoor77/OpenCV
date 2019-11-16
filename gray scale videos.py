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
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640,480))
while (cap.isOpened()):
    ret, frame = cap.read()
    out.write(frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("frame",gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()    
