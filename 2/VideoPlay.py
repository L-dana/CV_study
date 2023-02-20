import cv2 as cv 

#VideoCapture 의 요소로 불러올 동영상 파일 이름을 사용합니다.
cap = cv.VideoCapture("Video/풀무상 구현.mp4")

if cap.isOpened() == False:
    print("동영상 파일을 열 수 없습니다.")
    exit(1)

while(True):
    ret, img_frame = cap.read()

    #동영상을 끝까지 재생하면 read() 함수는 False 를 리턴합니다.
    if ret == False:
        print("동영상 파일 읽기 완료.")
        break;
    
    cv.imshow('Color',img_frame)

    #동영상 재생 속도를 조정하기 위해 waitKey()함수의 요소로 25밀리세컨드를 설정
    key = cv.waitKey(25)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()