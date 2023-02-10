#MergeStep 에서 이어짐.
#openCV 에서는 두 개의 이미지를 합쳐 하나로 만들 수 있는 hconcat() 함수와  vconcat() 함수를 제공
#hconcat() 함수는 수평방향으로 이미지 결합(두 이미지의 높이가 같아야 함)
#vconcat() 함수는 수직방향으로 이미지 결합(두 이미지의 너비가 같아야 함)
#두 함수 모두 이미지 타입이 같아야 결합 가능(2개의 이미지가 모두 컬러거나 그레이 스케일 이어야 함)

#그레이 스케일 이미지와 Canny를 사용해 에지를 검출한 결과 이미지를 하나로 만들어 보여준다.

import cv2 as cv
import sys

img_color = cv.imread('imgs/roffjrtlvhfem.PNG', cv.IMREAD_COLOR)

if img_color is None:
    print('이미지를 불러올 수 없음.')
    sys.exit(1)

#그레이 스케일 이미지로 변환
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

#Canny를 사용해 에지 검출
img_canny = cv.Canny(img_gray, 90, 180)


#연결할 이미지를 hconcat/vconcat 의 아규먼트로 입력
#같은 타입의 이미지여야 한다.

#수평 방향으로 이미지를 연결
img_result = cv.hconcat([img_gray, img_canny])

#수직 방향으로 이미지를 연결
img_result = cv.vconcat([img_gray, img_canny])

cv.imshow('Result', img_result)
cv.waitKey(0)

cv.destroyAllWindows()