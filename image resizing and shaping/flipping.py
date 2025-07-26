
import cv2
image=cv2.imread("img2.jpg")

# image size big hai esliye maine esko resize kr diya
resize=cv2.resize(image,(1540,900))

if image is not None:
    print("Image rotate successfully")

    # flipping horizontal
    flipped_horizontal=cv2.flip(resize,1)

    # flipping vertical
    flipped_vertical = cv2.flip(resize, 0)


    # flipping both
    flipped_both = cv2.flip(resize, -1)



    # original image
    cv2.imshow("original Image", resize)
    # show the horizontal flipping
    cv2.imshow("horizontal_flipping Image",flipped_horizontal)

    # show the vertical flipping
    cv2.imshow("vertical_flipping Image",flipped_vertical)

    # show the both flipping
    cv2.imshow("both_flipping Image",   flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not loaded")