# openCV에서 제공하는 GUI는 최소한의 기능만 제공한다.
# openCV 함수의 파라미터를 조정할 수 있는 트랙바와 사용자의 마우스/키보드 입력을 감지하는 기능만 제공한다.
# 좀 더 고급기능이 필요하다면 다른 GUI를 써야 한다.

# openCV에서 생성하는 윈도우에 트랙바를 추가해 함수 파라미터를 조정하는데 사용할 수 있다.(실시간 조정 가눙)
# 트랙바를 사용하여 이미지에서 물체의 에지를 검출하는데 사용하는 Canny함수의 파라미터를 조정한다.
# Canny 함수는 2개의 파라미터를 사용하여 검출되는 에지를 조정한다.

import cv2 as cv

#트랙바를 조정할 때마다 실행되는 콜백함수
#이곳에 트랙바로 조정할 openCV 함수를 넣을 수 있다.
#지금은 아무 동작이 없는 더미로 정의
def on_trackbar(x):
    pass

#namedWindow 함수를 사용하여 트랙바를 붙인 윈도우를 생성해야 합니다.
cv.namedWindow('Canny')

#트랙바를 생성한다.
#트랙바 이름, 윈도우 이름, 트랙바의 최소값, 트랙바의 최댓값, 콜백함수를 입력
cv.createTrackbar('low threshold', 'Canny', 0, 100, on_trackbar)
cv.createTrackbar('high threshold', 'Canny', 0, 500, on_trackbar)

#트랙바의 초기값을 설정해줍니다.
#트랙바 이름, 트랙바가 붙은 윈도우 이름으로 트랙바에 접근.
cv.setTrackbarPos('low threshold', 'Canny', 50)
cv.setTrackbarPos('high threshold', 'Canny' , 150)

#이미지를 그레이 스케일로 불러온다
#Canny 함수는 그레이 스케일로 입력해야 한다.
img_gray = cv.imread('imgs/roffjrtlvhfem.PNG', cv.IMREAD_GRAYSCALE)


#트랙바가 조정 시 Canny함수에 반영되도록 루프를 사용한다.
while(1):
    
    #현재 트랙바의 위치를 가져온다.
    low = cv.getTrackbarPos('low threshold', 'Canny')
    high = cv.getTrackbarPos('low threshold', 'Canny')

    #트랙바로부터 가져온 값으로 Canny함수의 파라미터를 조정
    img_canny = cv.Canny(img_gray, low, high)

    #Canny 함수의 실행 결과를 화면에 보여준다.
    cv.imshow('Canny', img_canny)

    #ESC 키를 누르면 루프를 종료
    if cv.waitKey(1) & 0xFF == 27:
        break



cv.destroyAllWindows()