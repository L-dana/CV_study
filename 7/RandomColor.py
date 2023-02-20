#이미지에 라벨링처럼 영역 분할 처리 후  구분을 위해 랜덤색을 사용할 필요가 있다.
 
#무작위로 색을 만들어서 픽셀별로 다른색을 출력한다.



import cv2 as cv
import numpy as np
from random import randint

#컬러 이미지를 위한 빈 넘파이 배열을 선언한다.
width = 640
height = 480

img = np.zeros((height, width, 3), np.uint8)

img_h = img.shape[0]
img_w = img.shape[1]

for y in range(img_h):
    for x in range(img_w):
        #픽셀별로 다른 값을 갖도록 0~255 사이의 값을 생성한다.
        img.itemset(y, x, 0, randint(0, 255)) #blue
        img.itemset(y, x, 1, randint(0, 255)) #green
        img.itemset(y, x, 2, randint(0, 255)) #red

cv.imshow('drawing', img)

cv.waitKey(0)