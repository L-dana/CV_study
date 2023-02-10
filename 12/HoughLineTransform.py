#허프 변환 Hough Line Transform
#이미지에서 직선을 찾기 위해 사용하는 알고리즘. 

#직선을 방정식으로 나타내면 y = mx + b 이다. 이 식을 매개변수식으로 바꾸면
#r = xCosθ + ySinθ 이다. 여기서 r 은 원점으로부터 직선까지의 수직 거리이며 
#θ는 이 직선과 수직인 직선과 x축 사이의 각도를 시계 반대 방향으로 측정한 값을 말한다.

#r = xCosθ + ySinθ 를 기반으로
#좌표 (300, 300) 을 지나는 모든 직선에 대한 r과 θ를 구해서 극좌표계 그래프를 그리면 사인 곡선이 나온다.
#r = xCosθ + ySinθ 에서 r = 300*Cosθ + 300*Sinθ 에 θ를 0~180 까지 증가시키면서 r을 구한 결과이다.

#좌표 (300, 300) (200, 200) (100, 100) 세 점을 지나는 모든 직선에 대한 r과 θ 를 구하여
#극좌표계에 그려보면 3개의 그래프(사인 곡선) 가 그려지는데 한 점에서 만나는 것을 확인할 수 있다.
#이 교차점의 r 과 θ 를 구해서 직선의 방정식으로 변환 후 그려보면 세 점을 지나는 직선을 관찰할 수 있다.

#따라서 사인 곡선의 교차점을 구하기 위해서 2차원 배열에 사인 곡선을 누적한 다음 일정 개수 이상
#사인 곡선이 교차한 지점의 r, θ 값을 사용하면 직선이 구해진다.

#openCV 에서는 Hough Line Transform 을 위해 HoughLinesP() 함수와 HoughLines() 함수를 제공한다.
#HoughLines() 는 앞에서 설명한 대로 극좌표에서 교차점 정보인 r, θ를 리턴한다 모든 점을 계산하기 때문에 오래 걸린다.


#(r과 θ)배열 = HoughLines(입력 이미지, Rho, Theta, threshold)
#입력 이미지는 8비트 바이너리 이미지여야 한다.
#Rho = r의 범위, 0~1사이의 실수를 입력한다.
#Theta = θ의 범위, 0~180 사이의 실수를 입력한다. 단위는 라디안
#threshold = 극좌표계에서 곡선이 만나는 기준, 값이 클 수록 정확도는 올라가지만 검출되는 직선 수는 줄어든다.


import cv2 as cv
import numpy as np
import math


img_src = cv.imread('imgs/miku.png', cv.IMREAD_GRAYSCALE)

img_edge = cv.Canny(img_src, 50, 150)

img_result = cv.cvtColor(img_edge, cv.COLOR_GRAY2BGR)

img_result_p = np.copy(img_result)
lines = cv.HoughLines(img_edge, 1, np.pi/180, 185)
#(r과 θ)배열 = HoughLines(입력 이미지, Rho, Theta, threshold)

if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a*rho
        y0 = b*rho

        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))

        cv.line(img_result, pt1, pt2, (0,0,255), 3)

cv.imshow('Source', img_src)
cv.imshow('Standard Hough Line Transform', img_result)

cv.waitKey(0)