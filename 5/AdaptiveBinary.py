# Binarization >> BinarizationImprovement >> AdaptiveBinary 순으로 이어짐.
# 이전처럼 하나의 값을 사용해서 전체를 이진화 하는 경우에는 
# 대상 이미지의 한쪽이 너무 어두운 경우 좋은결과를 얻기 힘들다.

# 밝기가 적당한 영역과 너무 어두운 영역을 동시에 만족시킬 수 있는 임계값이 없을 때는
# 적응형 이진화를 통해 해결 가능하다.

# 적응형 이진화 (Adaptive Thresholding) 는 이미지를 작은 영역으로 나누어 각 영역별로
# 다른 임계값을 사용하는 방법이다.
# openCV 에서는 적응형 이진화를 위해 adaptive Threshold 함수를 제공한다.

import cv2 as cv
import sys



#이미지를 읽어온다.
img_color = cv.imread('imgs/FT.png', cv.IMREAD_COLOR)
if img_color is None:
    print('이미지 파일을 읽을 수 없음. ')
    sys.exit(1)

#그레이 스케일 이미지로 변환한다.
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

#그레이 스케일 이미지에 적응형 이진화를 적용한다.
img_binary = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, 
cv.THRESH_BINARY_INV, 5, 4)
# cv.THRESH_BINARY_INV (검은배경 하얀선)
# cv.THRESH_BINARY (하얀배경 검은선)

#adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
#src – grayscale image(입력 이미지)
#src2 - binary image (출력 이미지)
#maxValue - 임계값을 넘으면 부여할 값.
#adaptiveMethod – 이진화 임계값을 결정하는 계산 방법(mean, gaussian 방식)
#thresholdType – threshold 방법 (THRESH_BINARY / THRESH_BINARY_INV)
#blockSize – thresholding을 적용할 영역 사이즈, 홀수(3, 5, 7, ...)
#C – 계산된 경계 값(평균이나 가중평균)에서 차감할 값

#Mean방식은 지정된 영역의 이웃 픽셀의 평균으로 threshold를 결정하는 방법
#Gaussian 방식은 가우시안 분포에 따른 가중치의 합으로 threshold를 결정하는 방법


#결과 이미지를 보여준다.
cv.imshow('Grayscale', img_gray)
cv.imshow('Binary', img_binary)
cv.waitKey(0)