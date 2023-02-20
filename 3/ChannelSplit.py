import cv2 as cv
# 컬러 이미지를 b, g, r 채널로 분리한 후, 순서를 r, g, b 순서로 바꿔서 컬러 이미지를 생성함


img_color = cv.imread("imgs/light.png", cv.IMREAD_COLOR)

#컬러 이미지를 채널별로 분리합니다.
img_b, img_g, img_r = cv.split(img_color)

#채널별 이미지를 조합하여 컬러 영상을 생성합니다.
#blue와 red의 순서를 바꾼다.
img_result = cv.merge((img_r, img_g, img_b))


cv.imshow('Color', img_result)
cv.imshow('B', img_b)
cv.imshow('G', img_g)
cv.imshow('R', img_r)

cv.waitKey(0)
cv.destroyAllWindows()