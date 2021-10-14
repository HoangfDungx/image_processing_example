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
    
    # Convert frame to grayscale frame
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display result
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

# Release capture
cap.release()
cv.destroyAllWindows()