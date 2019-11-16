# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 01:23:35 2019

@author: Owner
"""

import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        
cap.release()
cv2.destroyAllWindows()      