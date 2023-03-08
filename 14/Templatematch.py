# 템플릿 매칭 Template Match
# 주어진 템플릿 이미지와 일치하는 영역을 입력 이미지에서 찾는 방법.

# openCV 는 템플릿 매칭을 위해 matchTemplete() 함수를 제공하며, 6가지 방법이 있다
# 2차원 컨볼루션처럼 템플릿 이미지를 입력 이미지 위에서 이동하며 대응하는 픽셀을 비교한다(슬라이딩 윈도우)
# 상호상관함수랑 방법이 비슷
# 결과로 그레이스케일 이미지를 리턴한다




# matchTemplete(img, tem, result, flag)
# img = 입력 이미지(그레이스케일)
# tem = 비교 이미지(템플릿)

# result = 검출 결과 이미지
# img의 크기가 W X H 이고, tem의 크기가 w X h 이면 result 크기는 (W - w + 1) X (H - h +1).

# flag = 검출 방법 선택. 
# 최대값 사용 방법(최대값 위치 리턴)
# TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED
# 최소값 사용 방법(최소값 위치 리턴)
# TM_SQDIFF, TM_SQDIFF_NORMED




#TM_SQDIFF
#유사하면 0(검은색), 비유사하면 255를 반환,
#템플릿 영상에서 입력 영상의 부분 영상(같은 위치에 있는)의 픽셀를 뺀 것을 제곱하여 다 더한다

#TM_SQDIFF_NORMED
#위의 TM_SQDIFF 를 [0,1] 로 정규화한 것.

#TM_CCORR
#유사하면 255, 비유사하면 0을 반환,
#같은 위치의 (템플릿 영상의 픽셀값) * (부분 영상의 픽셀 값) 을 모두 더한다.

#TM_CCORR_NORMED
#위의 TM_CCORR 를 [0,1] 로 정규화한 것

#TM_CCOEFF
#밝기를 보정하고 TM_CCORR을 한것, 
#유사하면 255, 비유사하면 0을 반환

#TM_CCOEFF_NORMED
#가장 성능이 뛰어나지만 수식이 복잡해서 연산량이 많다.
#완전히 일치하면 1, 역일치하면 -1, 상호 연관성이 없으면 0을 반환




import cv2 as cv
import numpy as np


#템플릿 이미지를 검출할 이미지를 불러온다.
img_rgb = cv.imread('imgs/dcgallery.PNG')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)


#템플릿 이미지를 불러온다.
img_tem = cv.imread("imgs/ek.PNG", cv.IMREAD_GRAYSCALE)
w, h = img_tem.shape[:2]


#템플릿 매칭을 수행
res = cv.matchTemplate(img_gray, img_tem, cv.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)


#검출된 템플릿 이미지와 유사한 영역에 사각형을 그린다.
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(img_rgb, top_left, bottom_right, (0, 0, 255), 2)


cv.imshow('Reuslt', img_rgb)
cv.waitKey(0)