#openCV에서는 폴리곤을 그리는 함수인 polylines, fillpoly 함수를 제공한다.
#polylines(이미지, 다각형을 이루는 점(배열), 다각형의 수, bool close , 색, 두께);
# pts 가 이중포인터여서 여러 다각형을 저장 가능함. -> 저장할 다각형의 수를 명시해야 함.
# npts 는 각 다각형의 꼭짓점의 수를 가리킨다.
# close = true 이면 닫힌 도형을 그리고 false 이면 열린 도형을 그린다.

#폴리곤을 그리는 함수를 사용해 오각형 외곽선과 내부가 채워진 오각형을 그린다.



import numpy as np
import cv2 as cv

width = 640
height = 640
bpp = 3

#컬러 이미지를 저장할 Mat 객체를 생성환다.
img = np.zeros((height, width, bpp), np.uint8)

red = (0,0,255)
green = (0, 255, 0)
yellow = (0, 255, 255)

thickness = 2

#polylines 를 사용하면 내부가 채워지지 않은 폴리곤을 그린다.
#polylines 의 세번째 아규먼트를 False 로 하면 시작점과 끝점이 이어지지 않는다.
pts = np.array([[315, 50], [570, 240], [475, 550], [150, 550], [50, 240]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], False, red, thickness)

#polylines의 세번쨰 아규먼트를 True 로 하면 시작점과 끝점이 이어진다.
pts = np.array([[315, 160], [150, 280], [210, 480], [420, 480], [480, 280]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, green, thickness)

#fillpoly 를 사용하면 내부가 채워진 폴리곤을 그린다.
pts = np.array([[320, 245], [410, 315], [380, 415], [265, 415], [240, 315]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.fillPoly(img, [pts], yellow)

cv.imshow('result', img)
cv.waitKey(0)