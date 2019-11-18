# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 00:46:49 2019

@author: Zain Mansoor
"""
import cv2 

def nothing(x):
    print(x)

cv2.namedWindow('image')

cv2.createTrackbar('CP', 'image', 10, 400, nothing)

switch = "color/gray"
cv2.createTrackbar(switch, "image", 0, 1, nothing)


while(1):
    
    img = cv2.imread("lena.jpg",1)
    
    cp = cv2.getTrackbarPos('CP', 'image')
    s = cv2.getTrackbarPos(switch, "image")
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(cp), (50,100),font, 4, (2,0,255), 4)
    
    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    cv2.imshow("image", img)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()