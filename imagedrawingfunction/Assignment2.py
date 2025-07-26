import cv2

img_loc=input("Enter your file location :")

image=cv2.imread(img_loc)


print("1.line draw \n2.circle draw \n 3.rectangle draw \n 4.Add text")
ch=int(input("Enter your choice :"))

while True:
    if ch==1:
        pt1=(273,337)
        pt2=(481,337)

        cv2.line(image,pt1,pt2,(255,0,0),2)

        cv2.imshow("Output_lineimage",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        choiceforsave=int(input("if you want to save press 1: "))

        if choiceforsave==1:
            # save the image
            cv2.imwrite("line.png", image)
        else:
            print("not save")
    elif ch==2:
        ptr1 = (444, 66)
        ptr2 = (675, 349)

        cv2.rectangle(image, ptr1, ptr2, (0,0,255), 3)

        cv2.imshow("Output_rectangleimage",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        choiceforsave=int(input("if you want to save press 1: "))

        if choiceforsave == 1:
            # save the image
            cv2.imwrite("rectangle.png", image)
        else:
            print("not save")

    elif ch==3:
        center = (4040, 150)
        radius = 50

        color = (255, 0, 0)
        thickness = -1

        cv2.circle(image, center, radius, color, thickness)

        cv2.imshow("Output_circleimage",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        choiceforsave = int(input("if you want to save press 1: "))

        if choiceforsave == 1:
            # save the image
            cv2.imwrite("circle.png", image)
        else:
            print("not save")

    elif ch==4:
        cv2.putText(image, "im ashish", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 2)

        cv2.imshow("output_textmage", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        choiceforsave = int(input("if you want to save press 1: "))
        if choiceforsave == 1:
            # save the image
            cv2.imwrite("text.png", image)
        else:
            print("not save")

    if ch==5:
        break








