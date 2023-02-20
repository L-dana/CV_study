#openCV는 문자열을 출력하는 putText 함수를 제공한다.
#cv.putText(이미지, "내용", 좌표, font, 크기, 색, 두께);
 
#폰트와 글자색이 다른 4개의 문자열을 출력한다.


import numpy as np
import cv2 as cv

img_w = 640
img_h = 480
bpp = 3

#컬러 이미지를 저장할 Mat객체를 생성한다.
img = np.zeros((img_h, img_w, bpp), np.uint8)

red = (0,0,255)
green = (0, 255, 0)
yellow = (0, 255, 255)
white = (255, 255, 255)

#이미지 중앙을 기준으로 문자열을 배치하기 위해 사용한다.
center_x = int(img_w/2)
center_y = int(img_h/2)

#여러 폰트를 사용해서 글자를 출력해본다.
#FONT_ITALIC
#FONT_HERSHEY
#FONT_HERSHEY_COMPLEX
#FONT_HERSHEY_COMPLEX_SMALL
#FONT_HERSHEY_DUPLEX
#FONT_HERSHEY_SCRIPT_COMPLEX
#FONT_HERSHEY_SCRIPT_SIMPLEX  손글씨 스타일 폰트
#FONT_HERSHEY_SIMPLEX
#FONT_HERSHEY_TRIPLEX
thickness = 2

location = (center_x - 200, center_y - 100)
font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
fontScale = 3.5
#cv.putText(이미지, "내용", 좌표, font, 크기, 색, 두께);
cv.putText(img, "OpenCV", location, font, fontScale, yellow, thickness)

location = (center_x - 150, center_y +20)
font = cv.FONT_ITALIC
fontScale = 2
cv.putText(img, "Tutorial", location, font, fontScale, red, thickness)

location = (center_x - 250, center_y +100)
font = cv.FONT_HERSHEY_SIMPLEX
fontScale = 1.5
cv.putText(img, "exemple.com", location, font, fontScale, white, thickness)

location = (center_x - 130, center_y +150)
font = cv.FONT_HERSHEY_COMPLEX
fontScale = 1.2
cv.putText(img, "fnffnfndfnd", location, font, fontScale, green, thickness)

cv.imshow('DrawingText', img)
cv.waitKey(0)