import cv2

# Load cascades
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


        # crop the region (region of interest)(slicing)
        # सिर्फ grayscale image का face region
        roi_gray = gray[y:y + h, x:x + w]

        # original colored frame का face region
        roi_color = frame[y:y + h, x:x + w]


        # Detect eyes inside the face(esliye hm gray color ko parameter me dale hai )
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5)
        if len(eyes) > 0:
            cv2.putText(frame, "Eyes Detected", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 2)

        # Detect smile inside the face
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.1, 20)
        if len(smiles) > 0:
            cv2.putText(frame, "Smile Detected", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 255), 2)

    # Show the result
    cv2.imshow("Smart Face Detection", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
