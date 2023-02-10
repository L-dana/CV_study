# 웹캠 영상 중앙에 사각형 영역을 지정해 사각형 내부의 픽셀들의 평균색을 계산한다.


import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

while True:
    ret, img_color = capture.read()

    img_result = img_color.copy()

    height, width = img_color.shape[:2]
    center_x = int(width/2)
    center_y = int(height/2)

    #ROI 영역을 빨간색 사각형으로 표시한다.
    cv.rectangle(img_result, (center_x - 100, center_y -100), (center_x + 100,center_y + 100), (0, 0, 255),3)

    #ROI 한 영역을 구해서 평균을 구한다.
    img_roi = img_color[center_y - 100:center_y + 100, center_x - 100:center_x + 100]
    me = cv.mean(img_roi)

    #ROI에 대한 평균 픽셀값으로 채운 이미지를 생성한다.
    img_mean = np.zeros(img_roi.shape, dtype = np.uint8)
    img_mean[:] = (me[0], me[1], me[2])

    cv.imshow('mean', img_mean)
    cv.imshow('color', img_result)
    cv.imshow('roi', img_roi)

    key = cv.waitKey(1)
    if key == 27:
        break