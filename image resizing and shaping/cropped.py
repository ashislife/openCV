import cv2

image=cv2.imread("img2.jpg")

if image is not None:
    cropped=image[100:200,50:150]
    cv2.imshow("Cropped image",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




