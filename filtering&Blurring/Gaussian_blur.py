import cv2

image=cv2.imread("myimage.jpeg")
resize_img=cv2.resize(image,(800,400))


blurred=cv2.GaussianBlur(resize_img,(3,3),1)
resize_blurimg=cv2.resize(blurred,(800,400))




cv2.imshow("Original Image",resize_img)
cv2.imshow("Blurred Image",resize_blurimg)

cv2.waitKey(0)
cv2.destroyAllWindows()