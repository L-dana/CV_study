#openCV 에서는 원을 그리기 위한 circle 함수를 제공한다.
#circle(이미지, 중심좌표, 반지름, 색, 선굵기(-1이면 채우기) );

#초록색으로 내부가 채워진 반지름 10인 원과 빨간색 선으로 반지름 100인 원


import numpy as np
import cv2 as cv

#컬러 이미지를 저장할 넘파이 배열을 생성합니다.
width = 640
height = 480
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)

#(320, 240)이 중심인 반지름 10인 초록색으로 채워진 원을 그린다.
cv.circle(img, (320, 240), 10, (0, 255, 0), -1)

#(320, 240)이 중심인 반지름 100인 빨간색 원을 그린다.
cv.circle(img, (320, 240), 100, (0, 0, 255), 1)

cv.imshow('result', img)
cv.waitKey(0)