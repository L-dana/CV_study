#중간값 블러링 MedianBlurring 은 관심 화소 주변으로 지정한 커널 크기 내의 픽셀을 크기순으로
#정렬한 후 중간값을 뽑아서 결과 이미지의 픽셀값으로 사용한다.
#무작위 노이즈를 제거하는 데 효과적이다.
#하지만 에지가 있는 이미지는 결과 이미지에서 에지가 사라질 수 있다.


import cv2 as cv

img = cv.imread('imgs/noiseimg.png')
#img = imread("imgs/colornoise.jpg");
#img = imread("imgs/noisewb.png");

median = cv.medianBlur(img, 5)

cv.imshow('Original', img)
cv.imshow('Result', median)

cv.waitKey(0)
cv.destroyAllWindows()