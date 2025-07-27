import cv2

image=cv2.imread("flower.jpg",cv2.IMREAD_GRAYSCALE)

ret,thresh_image=cv2.threshold(image,125,255,cv2.THRESH_BINARY)

cv2.imshow("Original Image",image)
cv2.imshow("Threshold_Image",thresh_image)
cv2.waitKey(0)
cv2.destroyAllWindows()