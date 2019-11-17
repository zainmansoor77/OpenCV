# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 13:08:36 2019

@author: Zain Mansoor
"""
import cv2

img1 = cv2.imread("lena.jpg", 1)
img2 = cv2.imread("messi5.jpg", 1)

print(img1.shape)
print(img1.size)
print(img1.dtype)
cv2.imshow("image1",img2)

b, g, r = cv2.split(img1)
print(b)
print(g)
print(r)

img1 = cv2.merge((b, g, r))
ball = img2[280:340, 330:390]
img2[273:333, 100:160] = ball

cv2.imshow("image",img2)

img1 = cv2.resize(img1, (512,512))
img2 = cv2.resize(img2, (512,512))
cv2.imshow("image2", img1)
cv2.imshow("image3", img2)
#cv2.imshow("image1",img2)

dst = cv2.add(img1, img2)
cv2.imshow("image4", dst)

dst2 = cv2.addWeighted(img1,0.6,img2,0.4,0)
cv2.imshow("image5",dst2)

dst3 = cv2.addWeighted(img1,0.6,img2,0.4,2)
cv2.imshow("image6",dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()




