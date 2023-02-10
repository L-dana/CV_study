# 회전 행렬을 사용하면 이미지를 회전시킬 수 있다.
# openCV에서는 getRotationMatrix2D 함수를 사용해 회전행렬을 생성하고
# warpAffine 함수를 사용해 이미지에 회전 변형을 가한다. getRotationMatrix2D 함수는
# 배율 및 회전 중심 좌표가 추가된 회전행렬을 사용한다.

# 이미지를 반시계 방향으로 45도 회전시킨다.



import cv2 as cv

img_color = cv.imread('imgs/font.PNG', cv.IMREAD_COLOR)
cv.namedWindow('Color', cv.WINDOW_NORMAL)  #사이즈 조절을 가능하게 하기 위해 2번 인자를 노말로 줌 + 미리 윈도우 선언
cv.resizeWindow('Color', 854, 480)
cv.imshow('Color', img_color)

height, width = img_color.shape[:2]

#이미지 중앙을 중심으로 반시계 방향으로 45도 회전시키는 행렬을 생성한다.
m = cv.getRotationMatrix2D((width/2.0, height/2.0), 45, 1)
#cv.getRotationMatrix2D( (회전의 중심좌표), 회전 각도(양수가 반시계), 이미지 배율(1이면 원본) )

#회전 행렬 m을 이미지 img_color 에 적용한다.
img_rotation = cv.warpAffine(img_color, m, (width, height))

cv.imshow('Rotation', img_rotation)
cv.waitKey(0)

cv.destroyAllWindows()