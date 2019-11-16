# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:17:13 2019

@author: Zain Mansoor
"""

import cv2

img = cv2.imread("lena.jpg",1)
img = cv2.line(img,(0,0),(500,500),(85,78,26),5) 
#cv2.line(image,(initial position coordinate),(final position coordinate),(BGR color),thickness of line)
img = cv2.arrowedLine(img,(300,250),(500,500),(200,78,154),5)
#cv2.arrowedLine(image,(initial position coordinate),(final position coordinate),(BGR color),thickness of line)
img = cv2.rectangle(img,(188,230),(410,280),(76,198,95),5)
#cv2.rectangle(image,(initial coordinate of diagnal),(final coordinate of diagnal),(BGR color),thickness of rectangle's line)
img = cv2.circle(img,(200,100),80,(200,200,200),-1)
#cv2.circle(image,(coordinate of center of circle),length of radius,(BGR color),thickness of line)
cv2.imshow('image',img)

k = cv2.waitKey(0)
if k == ord(" "):
    cv2.destroyAllWindows()
elif k == ord("s"): 
    cv2.imwrite("lena_line.jpg",img)     
    cv2.destroyAllWindows()