#Subtracktion : 뺄셈
#차영상은 같은 장소를 촬영한 2장 이상의 이미지를 사용하여 새로 추가된 객체를 검출하는 방법이다.
#(역으로 배경을 추출할 수도 있음)
#같은 장소를 촬영하고 있는 상태에서 두 장의 이미지를 얻어야 한다.

#객체가 있는 이미지에서 배경만 찍은 이미지를 빼어 차영상을 얻는다.
#차영상을 구하면 2장의 이미지가 겹치는 부분이 보일 수도 있다



import cv2 as cv

#아이콘이 적을 때 이미지 iris1
#아이콘이 많을 때 이미지 iris2 를 그레이 스케일로 불러온다.
img_background = cv.imread('imgs/iris1.png', cv.IMREAD_GRAYSCALE)
img_object = cv.imread('imgs/iris2.png', cv.IMREAD_GRAYSCALE)

#아이콘이 많을 때 이미지 iris2
#아이콘이 적을 때 이미지 iris1 를 빼서 차영상을 얻는다. 
# 순서가 바뀌면 제대로 진행되지 않음.
img_subtraction = cv.subtract(img_object, img_background)

#차영상을 이진화한다.
retval, img_binary = cv.threshold(img_subtraction, 50, 255, cv.THRESH_BINARY)

#사이즈 조절을 위해 윈도우 창 미리 등록(옵션으로 WINDOW_NORMAL 필요)
#WINDOW_NORMAL 로 선언하면 마우스로 창 크기를 조정할 수도 있다.
cv.namedWindow("background",cv.WINDOW_NORMAL)
cv.namedWindow("object", cv.WINDOW_NORMAL)
cv.namedWindow("sub", cv.WINDOW_NORMAL)
cv.namedWindow("binary", cv.WINDOW_NORMAL)

#16:9 사이즈로 리사이즈(원본은 엄청 큼)
cv.resizeWindow("background", 854, 480)
cv.resizeWindow("object", 854, 480)
cv.resizeWindow("sub", 854, 480)
cv.resizeWindow("binary", 854, 480)


#이미지를 실제로 보여준다.
cv.imshow("background", img_background)
cv.imshow("object", img_object)
cv.imshow("sub", img_subtraction)
cv.imshow("binary", img_binary)

cv.waitKey(0)