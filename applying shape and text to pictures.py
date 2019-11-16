# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:35:50 2019

@author: Zain Mansoor
"""

import cv2

img = cv2.imread("lena.jpg",1)
img = cv2.line(img,(0,0),(200,300),(150,150,150),10)
img = cv2.arrowedLine(img,(300,250),(100,350),(150,150,150),10)
img = cv2.rectangle(img,(100,10),(200,100),(200,200,200),5)
img = cv2.rectangle(img,(200,110),(300,200),(200,100,20),-1)
img = cv2.circle(img,(250,250),70,(45,89,147),8)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,"hi lena",(0,500),font,3,(255,200,100),10,cv2.LINE_AA)
cv2.imshow("image",img)
k = cv2.waitKey(0)
if k & 0xFF == ord("s"):
    cv2.imwrite("manipulated.jpg",img) 
    cv2.destroyAllWindows()
else: #k & 0xFF == ord(" "):
    cv2.destroyAllWindows()