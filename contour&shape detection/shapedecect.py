import cv2

img=cv2.imread("trangle.png")

# 3-channel(BGR)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# threshold(light ,dark)
_,thresh=cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

# find contours(shape boundry find)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


# 3 chanal hote hai esliye parameter me 3 cloror pass kiye hai
cv2.drawContours(img,contours,-1,(255,0,0),2)


# detection
for contour in contours:
    # ye hamare shape ko pixels wise check karega
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    corners=len(approx)

    if corners==3:
        shape_name="Trangle"
    elif corners==4:
        shape_name="rectangle"
    elif corners==5:
        shape_name="Pentagone"
    elif corners>5:
        shape_name="Circle"
    else:
        shape_name="unknown"

    cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)

    # multidimension-> 1D
    x=approx.ravel()[0]
    y=approx.ravel()[1]-10

    cv2.putText(img,shape_name,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,0,0))

cv2.imshow("contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()