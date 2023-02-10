#openCV에서는 타원을 그리기 위한 ellipse 함수를 제공한다.
#ellipse(이미지, 중심좌표, 메인축의 반지름(x/y), 회전각도, 호의 시작각도, 호의 끝각도, 색, 선굵기);
#메인축의 반지름 = 중심좌표로부터 x축 y축을 따르는 반지름
#회전각도 = 90 으로 입력하면 수직으로 회전시켜서 그려준다.
#선굵기 = -1이면 꽉 채운다.
#나중에 그린 원이 가장 위로 간다.

#반지름 200인 원과 x, y 축 방향으로 각각 긴 타원 2개를 그린다.



import numpy as np
import cv2 as cv

#컬러 이미지를 저장할 넘파이 배열을 생성한다.
width = 640
height = 480
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)

center = (int (width/2), int(height/2))

#center 를 중심으로 하는 3개의 원을 그린다.
#ellipse(이미지, 중심좌표, 메인축의 반지름(x / y), 회전각도, 호의 시작각도, 호의 끝각도, 색, 선굵기)

#x축 방향 반지름 길이200, y축 방향 반지름 길이 10인 노란색 타원
cv.ellipse(img, center, (200, 10), 0, 0, 360, (0, 255, 255), 3)

#x축 방향 반지름 길이10, y축 방향 반지름 길이 200인 녹색 타원
cv.ellipse(img, center, (10, 200), 0, 0, 360, (0, 255, 0), 3)

#x축 방향 반지름 길이200, y축 방향 반지름 길이 200인 빨간색 타원
cv.ellipse(img, center, (200, 200), 0, 0, 360, (0, 0, 255), 3)

cv.imshow('result', img)
cv.waitKey(0)