import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error to open camera")
    exit()

while True:
    # Capture a frame
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Draw line:
    cv.line(frame,(50,50),(100,100),(255,0,0),5)
    # image, point 1, point 2, color, width (px)

    # Draw Rectangle
    cv.rectangle(frame,(50,50),(100,100),(0,255,0),3)

    # Draw Circle
    cv.circle(frame,(400,400),100,5)

    # Add text
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(frame,'hello world',(500,500), font, 4, (0,0,255),2,cv.LINE_AA)

    # Display result
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

# Release capture
cap.release()
cv.destroyAllWindows()