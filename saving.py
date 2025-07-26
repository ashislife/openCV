import cv2

image=cv2.imread("img.jpg")

if image is not None:
    success=cv2.imwrite("output_img.png",image)

    # save the edited file
    if success:
        print("Image saved successfully as 'output_img.png' ")
    else:
        print("failed to save as image ")
else:
    print("Error: could not load image")

