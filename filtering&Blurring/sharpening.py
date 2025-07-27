import cv2
import numpy as np


image=cv2.imread("myimage.jpeg")
resize_img=cv2.resize(image,(800,400))

sharpen_kernal=np.array([
    [0,-1,0],
    [-1,6,-1],
    [0,-1,0]

])

sharpening=cv2.filter2D(resize_img,-1,sharpen_kernal)
resize_sharp=cv2.resize(sharpening,(800,400))

cv2.imshow("Original Image",resize_img)
cv2.imshow("Resize_sharp Image",resize_sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()