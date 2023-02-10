#크기 조정(Scaling) 은 이미지의 크기를 원래 크기보다 크게 또는 작게 만드는 변환이다
#창 크기를 조정하는 resizeWindow() 와 다르게 이미지 자체의 크기를 건드린다.

#openCV에서는 이미지 크기 조정을 위해 resize 함수를 제공한다.
#resize(이미지, 결과 이미지, 결과 이미지 크기, 수평방향 조정비율, 수직방향 조정비율, 보간법)
#보간법을 지정할 수 있는데
#디폴트값은 INTER_LINEAR
#이미지 확대 시 INTER_CUBIC(좀더 선명한 이미지, 하지만 느린 속도) 또는 INTER_LINER(빠르지만 비교적 흐린 이미지)를 권장
#이미지 축소 시 INTER_AREA 를 권장



import cv2 as cv

#이미지를 불러온다.
img_color = cv.imread('imgs/battlemage.png', cv.IMREAD_COLOR)
cv.imshow('Original', img_color)

#fx, fy를 사용해 이미지 확대 및 축소비율을 적어줄 수 있다.
#resize(이미지, 결과 이미지 크기, 보간법) 또는
#resize(이미지, None, fx, fy, 보간법)

#지금은 가로방향(fx) 로 2배, 세로방향(fy) 로 2배로 확대한다.
#이미지 확대 시 INTER_CUBIC(좀더 선명한 이미지, 하지만 느린 속도) 또는 INTER_LINER(빠르지만 비교적 흐린 이미지)를 권장
img_result = cv.resize(img_color, None, fx = 2, fy = 2, interpolation = cv.INTER_CUBIC)
cv.imshow('x2 INTER_CUBIC', img_result)

#확대/축소되는 이미지 크기를 너비와 높이로 지정할 수 있다.
#지금은 너비와 높이를 3배 확대한다.
height, width = img_color.shape[:2]
img_result = cv.resize(img_color, (3 * width, 3 * height), interpolation = cv.INTER_LINEAR)
cv.imshow('x3 INTER_LINER', img_result)

#이미지의 너비와 높이를 0.5배로 줄인다.
img_result = cv.resize(img_color, None, fx = 0.5, fy = 0.5, interpolation = cv.INTER_AREA)
cv.imshow('x0.5 INTER_AREA', img_result)

cv.waitKey(0)
cv.destroyAllWindows()