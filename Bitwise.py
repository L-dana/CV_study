#openCV에서는 이미지를 대상으로 비트 연산을 수행하는 함수를 제공한다.

#and 연산을 사용해 왼쪽 사진의 요소를 오른쪽의 사진에 합성할 수 있다.
#우선 왼쪽 사진을 이진화한다. (배경을 지우고 합성하기 위해 2개의 이진화 이미지 필요)
#하나는 객체만 남기고 배경을 지우기 위해(객체 사진에서) / 나머지 하나는 배경에서 객체가 들어갈 부분만 배경을 지우기 위해(배경 사진에서)
 
#객체 이미지에서 배경을 지운 이미지, 배경 이미지에서 객체를 지운 이미지 두장이 있는 상태에서
#Bitwise and 연산 결과를 하나로 합치면 배경 이미지에 객체가 합성된다.

#마지막으로 원본 배경 이미지로 복사해준다.
#최종적으로 배경 이미지에 객체가 합성된다.


#bitwise_and 논리곱 - 이미지1과 이미지2의 값을 비트 단위로 파악하며, 해당 비트에 대해 AND 연산을 진행합니다.
#bitwise_or 논리합 - 이미지1과 이미지2의 값을 비트 단위로 파악하며, 해당 비트에 대해 OR 연산을 진행합니다.
#bitwise_xor 배타적 논리합 - 이미지1과 이미지2의 값을 비트 단위로 파악하며, 해당 비트에 대해 XOR 연산을 진행합니다.
#							 (XOR 연산은 비트 값이 같으면 0, 다르다면 1이 됩니다.)
#bitwise_not 부정 - 이미지의 값을 비트 단위로 파악하며, 해당 비트에 대해 NOT 연산을 진행합니다.



import cv2 as cv
import numpy as np

#사용할 이미지를 불러온다.
img_object = cv.imread('imgs/battlemage.PNG', cv.IMREAD_COLOR)
img_background = cv.imread('imgs/roffjrtlvhfem.PNG', cv.IMREAD_COLOR)

#객체를 이진화한다.
img_gray = cv.cvtColor(img_object, cv.COLOR_BGR2GRAY) #이진화를 위해 그레이 스케일로 변경
ret, img_mask = cv.threshold(img_gray, 180, 255, cv.THRESH_BINARY) #그레이 스케일 이미지에서 객체만 추출(객체만 1)


#배경을 지우고 객체만 배경 이미지에 보여주려면 반전된 이진화 이미지도 필요하다.
img_mask_inv = cv.bitwise_not(img_mask)  #객체 이미지에서 배경만 추출

#객체 이미지 크기만큼 배경 이미지를 잘라낸다.
#객체가 삽입될 위치가 된다.
height, width = img_object.shape[:2]
img_roi = img_background[0:height, 0:width]

#이진화 이미지를 사용해 객체 이미지에서는 배경을 지우고
#배경 이미지에서는 객체가 들어갈 위치를 지운다.
img1 = cv.bitwise_and(img_object, img_object, mask = img_mask_inv)
img2 = cv.bitwise_and(img_roi, img_roi, mask = img_mask)

#bitwise_and 함수를 사용한 결과를 더하면 배경 이미지에 로고가 합성된 결과가 나온다.
dst = cv.add(img1, img2)

#합성 결과를 배경 이미지에 복사해준다.
img_background[0:height, 0:width] = dst


#결과를 보여준다
cv.imshow("Object", img_object)
cv.imshow("Mask", img_mask)
cv.imshow("Mask_inv", img_mask_inv)
cv.imshow("img1", img1)
cv.imshow("img2", img2)
cv.imshow("dst", dst) #최종결과

cv.imshow("Background", img_background) #최종결과를 배경이미지에 넣음

cv.waitKey(0)