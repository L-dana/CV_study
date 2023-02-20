#파이썬에서도 이미지의 일부분을 지정하여 다른 변수에서 가리키게 할 수 있다.
#원본 이미지의 일부분을 ROI 넘파이 배열이 공유하게 된다.
#ROI 이미지에 선을 그리면 원본에도 선이 그어진다.
#하지만 이진화 같은 OpenCV함수를 적용한 후에는 서로 영향을 줄 수 없다.

import cv2 as cv

img_gray = cv.imread("imgs/Screenshot_20220617-191333.png", cv.IMREAD_GRAYSCALE)

#[start_y:end_y, start_x:end_y] 로 ROI영역을 지정합니다.
img_sub1 = img_gray[20:20+150, 20:20+150]

#img_sub1 이 img_color의 일부 데이터를 공유하기 때문에 True 가 리턴됩니다.
print(img_sub1.base is img_gray)

#같은 이미지 데이터를 공유하기 때문에 img_sub1 에 선을 그으면 img_gray 에도 선이 그어집니다.
cv.line(img_sub1, (0,0), (100,100), 0, 10)

ret, img_sub1 = cv.threshold(img_sub1, 127, 255, cv.THRESH_BINARY)

#img_sub1 이 입력과는 다른 넘파이 배열이 되므로  False 가 리턴됩니다.
print(img_sub1.base is img_gray)

#img_gray에는 영향을 주지 못하고 img_sub1 만 이진화 된다.
cv.imshow("img_gray", img_gray)
cv.imshow("img_sub1", img_sub1)

cv.waitKey(0)