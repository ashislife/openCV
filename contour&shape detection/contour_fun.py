import cv2

img=cv2.imread("trangle.png")

# 3-channel(BGR)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

# find contours
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


# 3 chanal hote hai esliye parameter me 3 cloror pass kiye hai
cv2.drawContours(img,contours,-1,(255,0,0),2)

cv2.imshow("contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()








#
# # not used-----------------------
#
# import cv2

# # 1-channel
# img=cv2.imread("trangle.png",cv2.IMREAD_GRAYSCALE)
#
#
# _,thresh=cv2.threshold(img,200,255,cv2.THRESH_BINARY)
#
# # find contours
# contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#
# cv2.drawContours(img,contours,-1,255,2)
#
# cv2.imshow("contours",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
# # -----------------<>----------------------------------------------------
# img: Grayscale image → sirf 1 channel → values 0 to 255.
#
# 255: White color (maximum intensity) for 1-channel image.
#
# Contours usi grayscale image pe draw ho jaate hain.
#
# 🔍 Output kya dikhega?
# Tumhare image me jitne bhi shapes (jaise triangle) honge, unke edges white line se draw ho jaayenge.
#
# Pura output image bhi black & white hi rahega (kyunki original bhi gray tha
#
# # -----------------<>----------------------------------------------------


