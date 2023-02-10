#대입 연산자를 사용하면 2개의 변스가 같은 넘파이 배열을 가리키게 됨
#이미지에 선을 그리는 것처럼 수정을 하는 경우에는 서로 영향을 주기 때문에 다른쪽에도 선이 그어진다.
#하지만 하나의 이미지에 이진화 같은 OpenCV 함수를 적용한 후에는 다른 넘파이 배열에 영향을 줄 수 없다.
#파이썬에서는 OpenCV 적용 전후의 넘파이 배열이 달라지기 때문이다.

#( C++ 에서는 입력시 사용한 Mat객체와 처리 후 반환되는 Mat 객체가 같지만 파이썬은 처리 전후 넘파이 배열이 다르다. )

import cv2 as cv

img_gray = cv.imread("imgs/Screenshot_20220617-191333.png", cv.IMREAD_GRAYSCALE)


#대입 연산자
img_copyed1 = img_gray

#img_gray와 img_copyed1 은 같은 넘파이 배열을 가리키게 됩니다.
#같은 넘파이 배열이므로 id함수의 리턴값이 같습니다.
print(id(img_gray), id(img_copyed1))

#아직은 같은 넘파이 배열을 가리키기 때문에 img_gray에 선을 그리면 img_copyed1 에서 선이 그려진다.
cv.line(img_gray, (100,100), (200,200), 0 ,10)

#img_gray 에 이진화를 적용하여 결과를 img_gray에 저장하면 
#img_gray와 img_copyed1 은 별개의 넘파이 배열을 가리키게 된다.
ret, img_gray = cv.threshold(img_gray, 127 ,255, cv.THRESH_BINARY)

#다른 객체가 되므로 id함수의 리턴값이 달라집니다.
print(id(img_gray), id(img_copyed1))

#img_copyed1 에는 영향을 주지 못하고 img_gray에만 이진화가 적용
cv.imshow("img_gray", img_gray)
cv.imshow("img_copted1", img_copyed1)

cv.waitKey(0)