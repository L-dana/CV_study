#openCV 에서는 이미지의 왼쪽 상단이 원점(0,0) 이다.
#오른쪽으로 갈수록 x 값이 증가하고, 아래로 내려갈수록 y값이 증가한다.

#컬러 이미지를 위한 Mat 객체를 생성 후 노란 원을 (100, 300) 에 그린다.
#좌표의 첫 원소가 x이고 두번째가 y임에 유의(이미지 픽셀은 (y,x) 임)



import numpy as np
import cv2 as cv

#컬러 이미지를 위한 빈 넘파이 배열을 생성
width = 640
height = 480

img = np.zeros((height, width, 3), np.uint8)

#이미지의 너비, 높이, 채널 수를 가져오는 방법
img_h = img.shape[0]
img_w = img.shape[1]
img_bpp = img.shape[2]

print(img_h, img_w, img_bpp)

#그리기 함수에서는 좌표를 (x, y) 순으로 적는다.
#(x, y) = (100, 300) 위치에 노란색 원을 그린다.
#circle(이미지, 중심좌표, 반지름, 색, 선두께)  선두께가-1 이면 속이 찬 원
cv.circle(img, (100, 300), 10, (0, 255, 255), -1)

cv.imshow('drawing', img)
cv.waitKey(0)