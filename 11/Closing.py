#모플로지 Morphology 는 보통 바이너리 이미지에서 흰색으로 나타나는 오브젝트 영역의
#형태를 개선하기 위해 사용한다. openCV 에서 제공하는 함수는
#Erosion, Dilation, Opening, Closing 등이 있다.

#Opening과 다르게 Dilation 다음에 Erosion을 적용한다. 
#이미지 상의 노이즈(작은 흰색 물체)를 제거하는데 사용한다.
#Erosion을 사용하면 노이즈(작은 흰색 오브젝트)가 없어지는데 흰색 오브젝트가 같이 작아진다.
#이때 Dilation을 적용하면 흰색 오브젝트가 원래 크기로 돌아온다.

#출력이미지 = morphologyEx(입력이미지, 수행할 작업, 커널)
#수행할 작업은 다음과 같이 넣는다.
#MORPH_OPEN = opening
#MOPPH_CLOSE = closing

#또한 커널 모양을 선택할 수 있다.
#MORPH_RECT = 사각형
#MORPH_ELLIPSE = 타원
#MORPH_CROSS = 십자가
#위 예시 이외에 여러 옵션이 있다.



import cv2 as cv
import numpy as np

img_gray = cv.imread('imgs/bin-1.png', cv.IMREAD_GRAYSCALE)

kernal = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
img_result = cv.morphologyEx(img_gray, cv.MORPH_CLOSE, kernal)

cv.namedWindow('Original', cv.WINDOW_NORMAL)
cv.namedWindow('Closing_Result', cv.WINDOW_NORMAL)

cv.imshow('Original', img_gray)
cv.imshow('Closing_Result', img_result)

cv.waitKey(0)
cv.destroyAllWindows()