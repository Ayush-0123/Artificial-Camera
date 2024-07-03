import cv2
import winsound
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
#cv2. absdiff is a function which helps in finding the absolute difference between the pixels of the two image arrays.
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
#gaussianbluur use for image smoothingimage processing, any sharp edges in images are smoothed while minimizing too much blurring.
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
#In thresholding, each pixel value is compared with the threshold value. If the pixel value is smaller than the threshold, it is set to 0(black photo generate), otherwise, it is set to a maximum value (generally 255 white).
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
#Morphological operations are a set of operations that process images based on shapes. They apply a structuring element to an input image and generate an output image.Basics of dilation: Increases the object area
    dilated = cv2.dilate(thresh, None, iterations=3)
#You can use findContours() method of cv2 library to find all boundary points(x,y) of an object in the image.
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
        winsound.PlaySound('Dragon Ball.wav', winsound.SND_ASYNC)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Motion Detection', frame1)
cam.release()
cv2.destroyAllWindows()
