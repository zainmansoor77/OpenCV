# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:09:43 2019

@author: Zain Mansoor
"""
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

fourcc =cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("Weidth & height in video.mp4",fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Width: " + str(cap.get(3)) + "  Height: "+str(cap.get(4))
        frame = cv2.putText(frame,text,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        
        out.write(frame)
        cv2.imshow("frame",frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
  
cap.release()
out.release()
cv2.destroyAllWindows()      
