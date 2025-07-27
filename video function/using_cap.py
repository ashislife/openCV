import cv2


# start the webcam
cap=cv2.VideoCapture(0)

while True:
    # if ret=True/False (Frame=image)
    # ek image ko camera me se read karna hai
    ret,Frame=cap.read()

    if not ret:
        print("could not read Frame")
        break
    #  jo image read hue hai usko display karega
    cv2.imshow("webcam Feed",Frame)

    #  agar user ne q pess kiya to camera hi band ho jayega
    if cv2.waitKey(1) & 0xFF==ord('q'):
        print("Quitting....")
        break

# camera ko band karne ke liye
cap.release()
cv2.destroyAllWindows()

