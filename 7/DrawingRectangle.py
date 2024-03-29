#openCV 에서는 사각형을 그리기 위한 Rectangle 함수를 제공한다.
#다음 두가지 방법으로 사각형을 그릴 수 있다.

#사각형의 두 좌표(왼쪽 위/오른쪽 아래) 사용
# img = rectangle(이미지, (왼쪽 위 좌표), (오른쪽 아래 좌표), 색(0, 255, 0), 선 굵기(-1 이면 채우기) )

#사각형의 왼쪽 위 좌표와 너비, 높이 사용
# img = rectangle(이미지, (왼쪽위x, 왼쪽위y, 너비, 높이), 색(255, 0, 255), 선 굵기(-1 이면 채우기) )



import numpy as np
import cv2 as cv

#컬러 이미지를 저장할 넘파이 배열을 생성한다.
width = 640
height = 480
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)

#사각형의 왼쪽 위 좌표가 (50, 50), 오른쪽 아래 좌표가(450, 450)인 선굵기 3의 빨간 사각형을 그린다.
cv.rectangle(img, (50, 50), (450, 450), (0, 0 ,255), 3)

#사각형의 왼쪽 위 좌표가 (150, 200), 오른쪽 아래 좌표가 (250, 300) 인 내부가 초록색인 사각형을 그린다.
cv.rectangle(img, (150, 200), (250, 300), (0, 255, 0), -1)

#왼쪽 위 좌표가(300, 150) 이고 너비가 50, 높이가 100인 마젠타색으로 찬 사각형
cv.rectangle(img, (300, 150, 50, 100), (255, 0, 255), -1)

cv.imshow('result', img)
cv.waitKey(0)