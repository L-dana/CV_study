#허프 변환 Hough Circle Transform
#이미지에서 원(타원)을 찾기 위해 사용하는 알고리즘. 

#원은 다음 식으로 나타낼 수 있다.
#(x - cx)^2 + (y - cy)^2 = r^2 
#(cx, cy) 는 원의 중심 좌표이며 r은 원의 반지름이다. 원을 나타내는 식에
#3개의 파라미터가 있기 때문에 hough transform을 사용하려면 3 차원 배열이 필요하지만
#그 방법은 비효율적이기 때문에 openCV에서는 에지의 그레디언트 정보를 사용하는
#Hough Gradient Method 를 사용한다.

#openCV 에서는 원 검출을 위해 HoughCircles() 함수를 사용한다.
#내부에 에지 검출이 포함되어 있기 때문에 에지 검출 결과를 입력할 필요가 없다.

#circles = HoughCircles(입력 이미지, method, dp, mindist, param1 =100, param2 =100, minrad =0, maxrad=0)
 
#입력 이미지 = 그레이 스케일 이미지여야 함
#circles = 발견한 원을 기록할 행렬, 각 행(가로줄)은 3개(x, y, radius) 또는 4개(x, y, radius, votes) 의 원소를 가진다.
#method = 원을 검출하는 방법, HOUGH_GRADIENT 만 사용할 수 있다.
#dp = 이미지 해상도에 대한 accumulator 해상도의 비율의 역수.
# dp =1 이면 배열 accumulator는 입력 이미지와 같은 해상도를 가진다.
# dp =2 이면 절반의 너비와 높이를 가지게 된다.

#mindist = 검출된 원 사이의 최소 거리. 이 값이 너무 크면 검출되지 못한 원이 생기며, 너무 작으면 인접한 원이 잘못 검출될수 있다.
#param1 = 지정한 원 검출 방법을 위한 파라미터, HOUGH_GRADIENT일 경우 캐니 에지 디텍터의 높은 이진화 값. 
#낮은 이진화 값은 0.5배 해서 사용하게 된다.
#param2 = 지정한 원 검출 방법을 위한 파라미터, HOUGH_GRADIENT일 경우 accumulator 이진화 값. 이 값이 너무 작으면 거짓 원이 검출된다.
#가장 큰 accumulator 값을 가지는 원이 먼저 리턴된다.
#minradius = 검출하려는 원의 최소 반지름. 크기를 알 수 없는 경우 0으로 지정하면 된다.
#maxradius = 검출하려는 원의 최대 반지름. 크기를 알 수 없는 경우 0 으로 지정하면 된다. 음수로 지정하면 원의 중심만 리턴.

#-처리 속도가 매우 느림(원 검출은 힘들다).




from re import M
import numpy as np
import cv2  as cv


#그레이 스케일로 입력 이미지를 불러온다.
img_gray = cv.imread('imgs/e4.jpg', cv.IMREAD_GRAYSCALE)
img_gray = cv.medianBlur(img_gray, 5)

#결과 이미지에 컬러 도형을 사용하기 위해 컬러로 변환한다.
img_color = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)


#원을 검출한다.
circles = cv.HoughCircles(img_gray, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2= 120, minRadius=0 ,maxRadius=0)
#circles = HoughCircles(입력 이미지, method, dp, mindist, param1 =100, param2 =100, minrad =0, maxrad=0)

#입력 이미지 = 그레이 스케일 이미지여야 함
#circles = 발견한 원을 기록할 행렬, 각 행(가로줄)은 3개(x, y, radius) 또는 4개(x, y, radius, votes) 의 원소를 가진다.
#method = 원을 검출하는 방법, HOUGH_GRADIENT 만 사용할 수 있다.
#dp = 이미지 해상도에 대한 accumulator 해상도의 비율의 역수.
# dp =1 이면 배열 accumulator는 입력 이미지와 같은 해상도를 가진다.
# dp =2 이면 절반의 너비와 높이를 가지게 된다.

#mindist = 검출된 원 사이의 최소 거리. 이 값이 너무 크면 검출되지 못한 원이 생기며, 너무 작으면 인접한 원이 잘못 검출될수 있다.
#param1 = 지정한 원 검출 방법을 위한 파라미터, HOUGH_GRADIENT일 경우 캐니 에지 디텍터의 높은 이진화 값. 
#낮은 이진화 값은 0.5배 해서 사용하게 된다.
#param2 = 지정한 원 검출 방법을 위한 파라미터, HOUGH_GRADIENT일 경우 accumulator 이진화 값. 이 값이 너무 작으면 거짓 원이 검출된다.
#가장 큰 accumulator 값을 가지는 원이 먼저 리턴된다.
#minradius = 검출하려는 원의 최소 반지름. 크기를 알 수 없는 경우 0으로 지정하면 된다.
#maxradius = 검출하려는 원의 최대 반지름. 크기를 알 수 없는 경우 0 으로 지정하면 된다. 음수로 지정하면 원의 중심만 리턴.
circles = np.uint16(np.around(circles)) #연산된 자료를 정리해준다.

#검출된 원에 빨간샋/초록색 원을 그려준다.
for c in circles[0,:]:
    center = (c[0], c[1])  #중심좌표
    radius = c[2]  #반지름

    #바깥원
    cv.circle(img_color, center, radius, (0, 255, 0), 2)

    #중심 원
    cv.circle(img_color, center, 2, (0, 0, 255), 3)


#검출 결과를 화면에 보여준다.
cv.imshow('detected circles', img_color)
cv.waitKey(0)
cv.destroyAllWindows()