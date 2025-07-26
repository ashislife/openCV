import cv2

image=cv2.imread("img2.jpg")

if image is None:
    print("Image not found ")
else:
    print("Image loaded ")

    # (width,height)
    resized=cv2.resize(image,(1540,900))
    cv2.imshow("Original Image ",image)
    cv2.imshow("Resized Image",resized)

    # save the output resize image
    cv2.imwrite("resize_output1.png",resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

