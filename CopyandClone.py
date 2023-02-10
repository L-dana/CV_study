#파이썬에서는 이미지를 저장하기 위해 넘파이 배열을 사용하기 때문에 
#이미지 복사 시 넘파이의 copy 메소드를 사용한다.
#새로운 메모리 공간에 이미지 데이터를 복사하기 때문에 한쪽 이미지에 선을 그어도 다른 이미지는 그대로이다.

import cv2 as cv

img_gray = cv.imread("imgs/Screenshot_20220617-191333.png", cv.IMREAD_GRAYSCALE)

#copy 메소드를 사용하여 img_gray 의 이미지 데이터를 복사합니다.
img_copyed1 = img_gray.copy()

#copy 메소드를 사용했기 때문에 img_gray와 img_copyed1 에 대한
#id 리턴값이 다르다. 별개의 넘파이 배열이 되었기 때문.
print(id(img_gray), id(img_copyed1))

cv.line(img_gray, (0,0), (100,100), 0, 10)

ret, img_gray = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

print(id(img_gray), id(img_copyed1))

cv.imshow("img_gray",img_gray)
cv.imshow("img_copyed1", img_copyed1)

cv.waitKey(0)