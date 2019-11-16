# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:09:52 2019

@author: Zain Mansoor
"""
import cv2
import datetime

cap = cv2.VideoCapture(0)
fourcc =cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("date and time in video.mp4",fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        date = str(datetime.datetime.now())
        frame = cv2.putText(frame,date,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        
        out.write(frame)
        cv2.imshow("frame",frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
  
cap.release()
out.release()
cv2.destroyAllWindows() 
