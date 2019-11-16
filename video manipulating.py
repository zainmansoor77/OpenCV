# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:14:56 2019

@author: Zain Mansoor
"""

import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("manipulated output video.mp4",fourcc,20.0,(640,480))

while True:
    ret, frame = cap.read()
    #cv2.imshow("frame", frame)
    frame = cv2.line(frame,(0,0),(200,300),(150,150,150),10)
    frame = cv2.arrowedLine(frame,(300,250),(100,350),(150,150,150),10)
    frame = cv2.rectangle(frame,(100,10),(200,100),(200,200,200),5)
    frame = cv2.rectangle(frame,(200,110),(300,200),(200,100,20),-1)
    frame = cv2.circle(frame,(250,250),70,(45,89,147),8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    frame = cv2.putText(frame,"hi lena",(0,400),font,3,(255,200,100),10,cv2.LINE_AA)
    
    out.write(frame)
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()

cv2.destroyAllWindows()