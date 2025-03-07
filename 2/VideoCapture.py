import cv2 as cv

#카메라에서 이미지를 캡처하기 위해서는 VideoCapture 객체를 생성하여
#카메라와 연결해야 합니다 카메라 인덱스를 요소로 사용합니다.
#PC에 처음으로 연결한 카메라의 인덱스는 0
#두번쨰로 연결한 카메라의 인덱스는 1.... 카메라의 연결 순서에 맞추어 접근할 때 사용하는 인덱스 부여
cap = cv.VideoCapture(1)

#카메라와 성공적으로 연결되었는지 체크합니다.
if cap.isOpened() == False:
    print("카메라와 연결할 수 없습니다. ")

#카메라에서 이미지 캡처와 윈도우에 이미지 보여주기를 반복하면 동영상처럼 보이게 됩니다.
while(True):
    
    #카메라에서 이미지를 읽어옵니다.
    ret, img_frame = cap.read()

    #ret 리턴값이 False이면 캡처가 실패한 것입니다.
    if ret == False:
        print("캡처 실패. ")
        break;
    
    #캡처된 이미지를 윈도우에 보여줍니다.
    cv.imshow('Color',img_frame)

    #사용자의 키보드 입력을 1밀리세컨드만큼 기다린 후 다음 줄을 시행합니다.
    #cv.waitKey(3) = 3밀리세컨드만큼 기다리기
    key = cv.waitKey(1) 

    #ESC키가 입력되었다면 반복을 중지합니다.
    if key == 27:
        break
    
#사용이 끝난 카메라와 연결을 종료합니다.
cap.release()
cv.destroyAllWindows()