#openCV 에서는 커널을 만들어서 컨볼루션 하는 번거로움을 줄이기 위해 평균 블러링하는 함수인
#blur 를 제공한다.

import cv2 as cv

img = cv.imread('imgs/dcgallery.PNG')
img_blur = cv.blur(img,(5,5))

cv.imshow('Original', img)
cv.imshow('Result', img_blur)

cv.waitKey(0)
cv.destroyAllWindows()