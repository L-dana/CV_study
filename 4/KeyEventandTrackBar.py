#키 이벤트와 트랙 바를 합체


# openCV에서 제공하는 GUI는 최소한의 기능만 제공한다.
# openCV 함수의 파라미터를 조정할 수 있는 트랙바와 사용자의 마우스/키보드 입력을 감지하는 기능만 제공한다.
# 좀 더 고급기능이 필요하다면 다른 GUI를 써야 한다.

# openCV에서 생성하는 윈도우에 트랙바를 추가해 함수 파라미터를 조정하는데 사용할 수 있다.(실시간 조정 가눙)
# 트랙바를 사용하여 이미지에서 물체의 에지를 검출하는데 사용하는 Canny함수의 파라미터를 조정한다.
# Canny 함수는 2개의 파라미터를 사용하여 검출되는 에지를 조정한다.



# openCV 에서는 키보드 입력을 받기 위해 waitKey() 함수를 제공한다.
# waitKey() 함수는 요소로 주어지는 시간동안 사용자의 키보드 입력을 기다린다.
# 0 이면 입력이 주어질 때까지 무제한으로 기다리고, 1이상이면 주어진 시간(ms) 동안 기다리고 다음줄에 있는 코드를 실행한다.

# 에지 검출을 처리하는 코드를 
# 키보드 입력에 따라 원하는 단계의 모습을 화면에 출력한다.
# 1이면 원본, 2이면 그레이 스케일, 3이면 에지검출을 보여준다.



import cv2 as cv
import sys

#트랙바를 조정할 때마다 실행되는 콜백함수
#이곳에 트랙바로 조정할 openCV 함수를 넣을 수 있다.
#지금은 아무 동작이 없는 더미로 정의
def on_trackbar(x):
    pass

cap = cv.VideoCapture(0)
if cap.isOpened() == False:
    print('카메라가 연결되지 않습니다.')
    sys.exit(1)

#보여줄 결과를 지정하기 위한 변수
step = 1

#트랙 바 반복생성을 막을 변수
TrackBarCtal = False

#namedWindow 함수를 사용하여 트랙바를 붙일 윈도우를 생성해야 합니다.
cv.namedWindow('Result')

while(True):

    #img_frame 변수에 대입된 이미지를 윈도우에 보여주게 됩니다.
    #처음에는 카메라에서 캡처된 컬러 이미지입니다.
    ret, img_frame = cap.read()

    if ret == False:
        print('캡처 실패. ')
        break

    #step이 2 이상이면 img_frame 에는 그레이 스케일 이미지가 대입된다.
    if step > 1:
        img_frame = cv.cvtColor(img_frame, cv.COLOR_BGR2GRAY)
        print('step 1')

        #step 이 3이면 img_frame 에는 에지 이미지가 대입됩니다.
        if step > 2:
        
            #step 이 4이면 img_frame 에는 에지 이미지가 대입됩니다.
            if step > 3:
                print('step 3')

                if TrackBarCtal == False:
                    #트랙바를 생성한다.
                    #트랙바 이름, 윈도우 이름, 트랙바의 최소값, 트랙바의 최댓값, 콜백함수를 입력
                    cv.createTrackbar('low threshold', 'Result', 0, 100, on_trackbar)
                    cv.createTrackbar('high threshold', 'Result', 0, 100, on_trackbar)

                    #트랙바의 초기값을 설정해줍니다.
                    #트랙바 이름, 트랙바가 붙은 윈도우 이름으로 트랙바에 접근.
                    cv.setTrackbarPos('low threshold', 'Result', 1)
                    cv.setTrackbarPos('high threshold', 'Result' , 5)
                    TrackBarCtal = True
                    print('scvvvvvvvv')

                #현재 트랙바의 위치를 가져온다.
                low = cv.getTrackbarPos('low threshold', 'Result')
                high = cv.getTrackbarPos('high threshold', 'Result')

                print(low,'///' , high)

                #트랙바로부터 가져온 값으로 Canny함수의 파라미터를 조정
                img_frame = cv.Canny(img_frame, low, high)
                
            img_frame = cv.Canny(img_frame, 30 ,90)
            print('step 2')




    #1ms 동안 키보드 입력을 대기합니다.
    key = cv.waitKey(1)


    #앞에서 처리된 결과에 따라 다른 이미지가 Result 윈도우에 보여지게 됩니다.
    cv.imshow('Result', img_frame)

    if key == 27:  #ESC 키
        break

    #입력된 키에 따라서 step 변수에 다른 값을 대입합니다.
    #파이썬에서는 ord 함수를 사용하여 문자를 아스키 코드로 바꿀수 있다.
    elif key == ord('1'):
        step = 1
    elif key == ord('2'):
        step = 2
    elif key == ord('3'):
        step = 3
    elif key == ord('4'):
        step = 4


cap.release()
cv.destroyAllWindows()