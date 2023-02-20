#openCV에서는 타원을 그리기 위한 ellipse 함수를 제공한다.
#ellipse(이미지, 중심좌표, 메인축의 반지름(x/y), 회전각도, 호의 시작각도, 호의 끝각도, 색, 선굵기);
#메인축의 반지름 = 중심좌표로부터 x축 y축을 따르는 반지름
#회전각도 = 90 으로 입력하면 수직으로 회전시켜서 그려준다.
#선굵기 = -1이면 꽉 채운다.
#나중에 그린 원이 가장 위로 간다.

#타원의 일부인 호를 그린다 ( 호 = arc )
#시계 방향으로 0~90 도 까지 호를 그린다. (0도의 위치가 중요함)



import numpy as np
import cv2 as cv

#컬러 이미지를 저장할 넘파이 배열을 생성한다.
width = 640
height = 480
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)

center = (int(width/2),int(height/2))

#타원을 시계 방향으로 0~90도 까지만 그린다.
cv.ellipse(img, center, (100,100), 0, 0, 90, (0, 0, 255), 3)

cv.imshow('result', img)
cv.waitKey(0)