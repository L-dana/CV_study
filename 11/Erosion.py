#모플로지 Morphology 는 보통 바이너리 이미지에서 흰색으로 나타나는 오브젝트 영역의
#형태를 개선하기 위해 사용한다. openCV 에서 제공하는 함수는
#Erosion, Dilation, Opening, Closing 등이 있다.

#Erosion 은 바이너리 이미지에서 흰색 오브젝트의 외곽 픽셀을 0(검은색) 으로 만든다.
#노이즈(작은 흰색 픽셀이나 물체) 를 제거하거나 붙어잇는 오브젝트를 분리하는데 사용하면 좋다.
#사용한 커널의 크기에 따라서 오브젝트 외곽에서 0이 되는 픽셀의 정도가 달라진다.

#커널의 크기를 특정 크기로 고정하고 반복해서 적용하여도 오브젝트 외곽에서 0이 되는 픽셀의 정도를 조절해서
#비슷한 결과를 얻을 수 있다.

#Mat kernal = getStructuringElement(MORPH_RECT, Size(3,3));
#img_result = erode(img_gray, kernal, iterations = 1);
#iterations 는 반복 횟수이다. 디폴트는 1

#마스크(커널) 을 컨볼루젼했을때 마스크 내부 픽셀의 값 중에서 가장 최소값을 가지는 픽셀값을 해당 위치에 적용하게 된다.
# 210  0  29
# 255 255 9
# 62  34  0 
# 위와 같이 값이 있다면 최소값인 0 이 적용된다. 따라서 바이너리 이미지를 넣으면 0이 침식해서 들어가는 모습이 보인다.



import cv2 as cv
import numpy as np

#img_gray = cv.imread('imgs/miku.png', cv.IMREAD_GRAYSCALE)
img_gray = cv.imread("imgs/bin-1.png", cv.IMREAD_GRAYSCALE)

kernal = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
img_result = cv.erode(img_gray, kernal, iterations= 4)
#Point(-1, -1) 은 중앙을 뜻하며 커널이 적용될 때, 변경될 픽셀의 위치를 말한다.

cv.namedWindow('Original', cv.WINDOW_NORMAL)
cv.namedWindow('Result', cv.WINDOW_NORMAL)

cv.imshow('Original', img_gray)
cv.imshow('Result', img_result)

#cv.imwrite("e7.jpg", img_result)

cv.waitKey(0)
cv.destroyAllWindows()