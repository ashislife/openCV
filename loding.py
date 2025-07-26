import cv2

image=cv2.imread("img.jpg")

if image is None:
    print("Error: Image not found ")
else:
    print("Image loading successfully")
    