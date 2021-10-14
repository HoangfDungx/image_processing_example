import cv2 as cv
import sys

# declare path of image
path = "/home/hoangdung/Desktop/Image Processing/Introduction/hello_world.png"

## read image, data would be stored in type of cv.mat
# this is original image
img = cv.imread(path)

# this is grayscale image
img_gray_scale = cv.imread(path, 0)
# or
# img_gray_scale = cv.imread(path, cv.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("Read image fail")

cv.imshow("Image display", img)
cv.imshow("Grey scale image display", img_gray_scale)

k = cv.waitKey(0)

## Save image

cv.imwrite(path, img_gray_scale)