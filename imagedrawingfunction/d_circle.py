
import cv2
image=cv2.imread("planeimage.png")

if image is None:
    print("Oops your image is not working")

else:
    print("Image loaded successfully")

    center=(4040,150)
    radius=50

    color=(255,0,0)
    thickness=-1

    # circle draw in image
    cv2.circle(image,center,radius,color,thickness)

#     show
    cv2.imshow("output_image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
