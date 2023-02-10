#컬러 이미지의 픽셀에 접근해 그레이 스케일 이미지로 변환(색 빼기)
#cvtColor() 함수를 사용해 컬러 이미지로 변환(초록색 사각형을 그리기 위한 밑작업)
#/마지막으로 다시 픽셀에 접근해 초록색 사각형을 그림

#결과물 >> 원본 사진과 똑같은 흑백 사진 위에 초록색 사각형이 그려짐

import cv2 as cv
import numpy as np

img_color = cv.imread("imgs/roffjrtlvhfem.PNG", cv.IMREAD_COLOR) 
#이미지 파일명이 한글이면 읽을 수 없음, 추가 처리가 필요함.


#이미지의 높이와 너비를 가져옵니다.
height, width = img_color.shape[:2]

#그레이 스케일 이미지를 저장할 넘파이 배열을 생성합니다.
img_gray = np.zeros((height,width), np.uint8)

#for 문을 돌면서 (y, x)에 있는 픽셀을 하나씩 접근합니다.
for y in range(0, height):
    for x in range(0, width):

        #컬러 이미지의 (y, x)에 있는 픽셀의 b, g, r 채널을 읽습니다.
        b = img_color.item(y, x, 0)
        g = img_color.item(y, x, 1)
        r = img_color.item(y, x, 2)

        #(y, x) 위치의 픽셀에 그레이 스케일 값이 저장된다.
        #평균값을 쓰는 경우 gray = int((b + g + r)/3.0)
        #BT.709 에 명시된 값을 쓰는 경우 (김프 , 포토샵의 방법)
        gray = int(r*0.2126 + g*0.7152 + b*0.0722)

        img_gray.itemset(y,x, gray)


#결과 이미지에 컬러표시를 하기 위해 다시 컬러이미지로 변환한다.
img_result = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)

#y범위가 200~400, x범위가 200~300 인 영역의 픽셀을 특정 색으로 변경
for y in range(200, 400):
    for x in range(200, 300):

        img_result.itemset(y, x, 0, 249) #b
        img_result.itemset(y, x, 1, 177) #g
        img_result.itemset(y, x, 2, 197) #r


cv.imshow('color', img_color)
cv.imshow('result', img_result)

cv.waitKey(0)

cv.destroyAllWindows()