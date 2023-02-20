#실시간으로 ROI를 해서 선택한 영역에 캐니 에지를 적용해본다.
#이 방법은 좌상단에서 우하단으로 드래그하는 방법으로만 영역 선택이 가능하다.
#좀 더 개선된 영역 선택을 하려면 selectROI 함수를 이용할 것.


import cv2 as cv

mouse_is_pressing = False
start_x, start_y, end_x, end_y = 0,0,0,0
step = 0

def swap(v1, v2):
    temp = v1
    v1 = v2
    v2 = temp

#마우스 이벤트 콜백함수.
def mouse_callback(event, x, y, flags, param):
    #마우스 왼쪽 버튼을 누르면 ROI시작점이 된다.
	#마우스 왼쪽 버튼을 떼면 ROI끝점이 된다.
	#마우스 이동 시 ROI영역을 초록색 사각형으로 보여준다.
    global step ,start_x, start_y, end_x, end_y, mouse_is_pressing

    if event == cv.EVENT_LBUTTONDOWN:
        step = 1
        
        mouse_is_pressing = True
        start_x = x
        start_y = y

    elif event == cv.EVENT_MOUSEMOVE:
        if mouse_is_pressing:
            end_x = x
            end_y = y
            step = 2
       
    elif event == cv.EVENT_LBUTTONUP:
        mouse_is_pressing = False

        end_x = x
        end_y = y
        
        step = 3


cap = cv.VideoCapture(0)
if cap.isOpened() == False:
    print('카메라와 연결할 수 없습니다. ')
    exit(-1)

cv.namedWindow('ColorCam')
cv.setMouseCallback('ColorCam', mouse_callback)

while True:

    ret, img_color = cap.read() 
    #read() 함수는 ret 과 이미지를 리턴하는데 이미지를 읽는데 실패하면 
    #ret 는 False 가 된다.
    if ret == False:
        print('캡처 실패. ')
        break

    if step == 1:
        cv.circle(img_color, (start_x, start_y), 10, (0, 255, 0), -1)
			
    elif step == 2:
        #왼쪽 버튼을 누르고 움직이면 선택된 영역을 초록색 사각형으로 보여준다.
        cv.rectangle(img_color, (start_x, start_y), (end_x, end_y), (0, 255, 0), 3)

    elif step == 3:

        if start_x > end_x:
            swap(start_x, end_x)
            swap(start_y, end_y)
        
        #마우스 왼쪽 버튼에서 손을 떼고 나서 ROI를 지정한다.
        #ROI는 다음처럼 지정한다.
        #시작y : 끝y , 시작x : 끝x 
        ROI = img_color[start_y:end_y, start_x:end_x]

        ROI = cv.cvtColor(ROI, cv.COLOR_BGR2GRAY)
        ROI = cv.Canny(ROI, 150, 50)
        ROI = cv.cvtColor(ROI, cv.COLOR_GRAY2BGR)

        #원본 영상에 ROI영역을 복사한다.
        img_color[start_y:end_y, start_x:end_x] = ROI

        if cv.waitKey(1) == ord('1'):
            step = 0
            #break
    

    cv.imshow('ColorCam', img_color)
    if cv.waitKey(5) == 27:
        break