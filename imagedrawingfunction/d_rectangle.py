
import cv2
image=cv2.imread("planeimage.png")

if image is None:
    print("Oops your image is not working")

else:
    print("Image loaded successfully")

    ptr1=(444,66)
    ptr2=(675,349)

    color=(255,0,0)
    thickness=4

    # rectangle line draw in image
    cv2.rectangle(image,ptr1,ptr2,color,thickness)

#     show
    cv2.imshow("output_image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
