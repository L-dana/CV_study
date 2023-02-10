#모플로지 Morphology 는 보통 바이너리 이미지에서 흰색으로 나타나는 오브젝트 영역의
#형태를 개선하기 위해 사용한다. openCV 에서 제공하는 함수는
#Erosion, Dilation, Opening, Closing 등이 있다.

#Dilation 은 Erosion과 반대로 동작한다.
#바이너리 이미지에서 흰색 오브젝트의 외곽 픽셀 주변에 흰색 픽셀을 추가한다.
#노이즈를 제거하기 위해 사용한 Erosion 에 의해 작아진 오브젝트를 되돌리거나 인접한 오브젝트를 연결하기 위해서 사용한다.
#사용한 커널의 크기에 따라서 오브젝트 외곽에서 1이 되는 픽셀의 정도가 달라진다.

#커널의 크기를 특정 크기로 고정하고 반복해서 적용하여도 오브젝트 외곽에서 1이 되는 픽셀의 정도를 조절해서
#비슷한 결과를 얻을 수 있다.

#Mat kernal = getStructuringElement(MORPH_RECT, Size(3,3))
#dilate(img_gray, kernal, iterations = 1)
#iterations 는 반복 횟수이다. 디폴트는 1

#마스크(커널) 을 컨볼루젼했을때 마스크 내부 픽셀의 값 중에서 가장 높은 값을 가지는 픽셀값을 해당 위치에 적용하게 된다.
# 210  0  29
# 255 255 9
# 62  34  0 
# 위와 같이 값이 있다면 최대값인 255 이 적용된다. 따라서 바이너리 이미지를 넣으면 1이 점점 늘어나는 모습을 보임.



import cv2 as cv
import numpy as np

#img_gray = cv.imread('imgs/miku.png', cv.IMREAD_GRAYSCALE)
img_gray = cv.imread("imgs/bin-1.png", cv.IMREAD_GRAYSCALE)

kernal = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
img_result = cv.dilate(img_gray, kernal, iterations = 7)
#dilate(img_gray, kernal, iterations = 1)
#iterations 는 반복 횟수이다. 디폴트는 1

cv.namedWindow('Original', cv.WINDOW_NORMAL)
cv.namedWindow('Result', cv.WINDOW_NORMAL)

cv.imshow('Original', img_gray)
cv.imshow('Result', img_result)

#cv.imwrite("d7.jpg", img_result)

cv.waitKey(0)
cv.destroyAllWindows()