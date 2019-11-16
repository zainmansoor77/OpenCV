#import openCV library
import cv2

#read image from "lena.jpg" in color scale and convert it into matrix
img = cv2.imread("lena.jpg" , 1)

#disply image (convert matrix back to image)
cv2.imshow("image",img)
k = cv2.waitKey(0)

if k == ord(" ") :
        cv2.destroyAllWindows()
        
elif k == ord("s"):
    #imwrite convert img matrix back into image and save it by "lena_copy.png" name.
    cv2.imwrite("lena_copy.png",img)    
    #destroyAllWindows will terminate the image window
    cv2.destroyAllWindows()