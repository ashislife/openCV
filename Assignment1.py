import cv2
image=input("Enter the image location :")
# load user input location
image_loc=cv2.imread(image)
gray=cv2.cvtColor(image_loc,cv2.COLOR_BGR2GRAY)

choice=int(input("peess 1.show 2.save : "))
while True:
    if choice==1:
        cv2.imshow("Image title",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice==2:
        if image_loc is not None:
            success = cv2.imwrite("output1_img.jpg", gray)
    else:
        print("check Again!!!!")

    if choice==3:
        break












