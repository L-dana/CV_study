#블러링 Blurring 은 보통 이미지에서 노이즈를 제거하기 위해 사용한다.
#노이즈가 사라지면서 동시에 이미지가 흐려지게 된다.
#openCV 에서는 컨볼루션을 쉽게 할 수 있도록 filter2D 함수를 제공한다.
#커널을 정의하면 쉽게 컨볼루션 계산을 할 수 있다. 

#입력 이미지의 현재 위치에서 5x5 범위의 주변 픽셀값의 평균을 구해서 결과 이미지의 픽셀 값으로 입력한다.


import cv2 as cv
import numpy as np

img = cv.imread('imgs/dcgallery.PNG')
kernal = np.ones((5,5), np.float32)/25
dst = cv.filter2D(img, -1, kernal)

cv.imshow('Original', img)
cv.imshow('Result', dst)

cv.waitKey(0)
cv.destroyAllWindows()