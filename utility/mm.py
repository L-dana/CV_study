import os, sys
import numpy as np
import cv2 as cv

#img returned [h,w,3]
def read_image(src):
    img_array = np.fromfile(src, np.uint8)
    img = cv.imdecode(img_array, cv.IMREAD_COLOR)

    return img


def write_image(dst, img, params=None):
    try:
        ext = os.path.splitext(dst)[1]
        result, n = cv.imencode(ext, img, params)


        if result:
            with open(dst, mode='w+b') as f:
                n.tofile(f)
            return True

        else:
            return False

    except Exception as e:

        print(e)
        return False


# Function to remove background
def rmbg_fn(img):

    #트랙바를 조정할 때마다 실행되는 콜백함수
    #이곳에 트랙바로 조정할 openCV 함수를 넣을 수 있다.
    #지금은 아무 동작이 없는 더미로 정의
    def on_trackbar(x):
        pass

    #namedWindow 함수를 사용하여 트랙바를 붙인 윈도우를 생성해야 합니다.
    cv.namedWindow('Canny', cv.WINDOW_NORMAL)
    cv.resizeWindow("Canny", 854, 480)

    #트랙바를 생성한다.
    #트랙바 이름, 윈도우 이름, 트랙바의 최소값, 트랙바의 최댓값, 콜백함수를 입력
    cv.createTrackbar('low threshold', 'Canny', 0, 100, on_trackbar)
    cv.createTrackbar('high threshold', 'Canny', 0, 500, on_trackbar)

    #트랙바의 초기값을 설정해줍니다.
    #트랙바 이름, 트랙바가 붙은 윈도우 이름으로 트랙바에 접근.
    cv.setTrackbarPos('low threshold', 'Canny', 50)
    cv.setTrackbarPos('high threshold', 'Canny' , 150)

    #이미지를 그레이 스케일로 변환
    #Canny 함수는 그레이 스케일로 입력해야 한다.
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

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
        key = cv.waitKey(10)
        if key == 27:
            write_image(ns[0] + '_canny.png', ~img_canny)
            break


    #cv.destroyAllWindows()
    cv.destroyWindow('Canny')

    return img_canny


def apply(src):
    print("abgremoving on ", src)

    img_tar = read_image(src)  ##읽고
    rmbg_fn(img_tar)  ##처리


if __name__ == "__main__":
    input_list = sys.argv
    if len(input_list) <= 1:

        input('파일을 드래그 드랍해')

    src_list = input_list[1:]

    for src in src_list:
        ns = src.split(".")

        print(ns)
        result = apply(src) ## 프로세싱


    print("끝!")
    input('press enter to quit')