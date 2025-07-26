# import cv2
#
# image=cv2.imread("img2.jpg")
#
#
# if image is not None:
#     print("Image rotate successfully")
#
#     # rotate the image
#     (h,w)=image.shape[:2]
#     center=(w//2,h//2)
#     M=cv2.getRotationMatrix2D(center,90,1.0)
#     rotated_img=cv2.warpAffine(image,M,(w,h))
#
#     # show the image
#     cv2.imshow("Rotated Image",rotated_img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
# else:
#     print("Image not loaded")






# After resize the image
import cv2
image=cv2.imread("img2.jpg")
resize=cv2.resize(image,(1540,900))

if image is not None:
    print("Image rotate successfully")

    center=(1540//2,900//2)
    M=cv2.getRotationMatrix2D(center,90,1.0)
    rotated_img=cv2.warpAffine(resize,M,(1540,900))

    # show the image
    cv2.imshow("Rotated Image",rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not loaded")