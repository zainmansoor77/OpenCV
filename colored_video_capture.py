# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 01:23:35 2019

@author: Zain Mansoor
"""

import cv2

cap = cv2.VideoCapture(0)
count = 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.line(frame,(0,0),(500,500),(85,78,26),5)
    if ret == True:
        #print(1)
        while True:
            if count == 0:
                print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                count += 1
            else:
                break
        #ret, frame = cap.read()
        out.write(frame)
        cv2.imshow("frame",frame)
                
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
           
        
cap.release()
out.release()
cv2.destroyAllWindows()      