import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)

while True:
    ret,Frame=cap.read()

    gray=cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)

    '''detectMultiScale():scan and detect object face'''
    detect_faces=face_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in detect_faces:
        # draw rectangle
        cv2.rectangle(Frame,(x,y),(x+w,y+h),(0,255,0),2)


        cv2.imshow("webcam face detection",Frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

