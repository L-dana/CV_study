#openCV 함수 처리 결과를 단계별로 다른 윈도우에 보여줄 수 있다.
#처음 실행 시 윈도우의 위치를 잡아 놓으면 다음 번 실행시에도 윈도우 위치가 일정하게 유지

import cv2 as cv
import sys

img_color = cv.imread('imgs/roffjrtlvhfem.PNG', cv.IMREAD_COLOR)

if img_color is None:
    print('이미지 파일을 읽을 수 없음.')
    sys.exit(1)

#그레이 스케일 이미지로 변환
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

#Canny를 사용해 에지 검출
img_canny = cv.Canny(img_gray, 90, 180)

#윈도우별로 처리 결과를 보여준다
cv.imshow('Grayscale', img_gray)
cv.imshow('Cannny', img_canny)

cv.waitKey(0)
cv.destroyAllWindows()