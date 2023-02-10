#이동 Translation 은 이미지의 모든 점을 같은 방향으로 같은 거리로 이동시키는 변환이다.

#이동 행렬을 작성한 후 waroAffine 함수를 사용하여 이미지에 적용한다.
#이미지를 x축 방향으로 100, y축 방향으로 50 이동시킨다.


import cv2 as cv
import numpy as np

#이미지를 불러온다.
img_color = cv.imread('imgs/roffjrtlvhfem.PNG', cv.IMREAD_COLOR)
cv.imshow('Original', img_color)

height, width = img_color.shape[:2]

#이미지를 오른쪽으로 100, 아래로 50 이동시키는 이동 행렬을 만든다.
m = np.float32([[1, 0, 100],[0, 1, 50]])
# [1 0 100]
# [0 1  50]
# 2행 3열 행렬

#이동 행렬을 이미지에 적용한다.
img_translation = cv.warpAffine(img_color, m, (width, height))

cv.imshow('Translation', img_translation)

cv.waitKey(0)
cv.destroyAllWindows()