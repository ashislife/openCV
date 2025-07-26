
import cv2
image=cv2.imread("planeimage.png")

if image is None:
    print("Oops your image is not working")

else:
    print("Image loaded successfully")

    # rectangle line draw in image
    cv2.putText(image,"im ashish",(200,200),cv2.FONT_HERSHEY_SIMPLEX,1.3,(0,255,0),2)

    # show
    cv2.imshow("output_image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
