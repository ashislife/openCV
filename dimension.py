import cv2

image=cv2.imread("img.jpg")


if image is not None:
    h ,w ,c=image.shape
    print(f"Image loaded:\n Height:{h}\nWidth:{w}\nColor channel:{c}")

else:
    print("Could not load image")
