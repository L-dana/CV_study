#캐니 에지 디텍터는 1986년 존F.캐니에 의해서 개발되었다. 다음 3가지를 만족하는 것을 목표로 한다.

#낮은 에러율 - 실제 에지가 검출되어야 한다. 노이즈로 거짓 에지가 검출되선 안된다.
#정확한 에지 위치 - 캐니 에지와 실제 이미지의 에지 사이의 거리가 최소화되어야 한다.
#응답 최소화 - 실제 이미지상의 에지에서 하나의 에지만 검출되어야 한다.

#캐니 에지 디텍터를 사용하면 2개의 임계값을 사용하여 한 픽셀로 구성된 에지를 검출한다.

#Canny(input img, threshold_1, threshold_2, 마스크 크기)
#마스크 크기 = 소벨 연산에서 사용할 마스크의 크기를 말한다.


import cv2 as cv


img_gray = cv.imread('imgs/iris2.png', cv.IMREAD_GRAYSCALE)
cv.imshow('Original', img_gray)

#블러링을 적용한 후 캐니 에지 디텍터를 적용합니다.
img_gray = cv.blur(img_gray, (3,3))
#보통 첫 번째 임계값의 2~3 배 정도로 두번째 임계값을 정한다.
img_canny = cv.Canny(img_gray, 50, 120, 3)
cv.imshow('Canny Edge', img_canny)

cv.waitKey(0)
cv.destroyAllWindows()