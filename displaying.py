import cv2

image=cv2.imread("img1.jpg")

if image is not None:
    # open the window
    cv2.imshow("Image showing ",image)

    # wait for a key
    cv2.waitKey(0)

    # close window
    cv2.destroyAllWindows()

else:
    print("Could not load the image ")