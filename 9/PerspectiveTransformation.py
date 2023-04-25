#퍼스펙티브 변환 Perspective Transformation 에서 원본 이미지의 모든 직선은 출력 이미지에서 직선으로 유지된다.
#3차원의 공간에 있는 물체를 2차원 평면에 올리는 기술이라고 볼 수 있다.
#원근 변환 이라고도 한다.

#퍼스펙티브 변환 행렬을 찾으려면 입력 이미지의 네 점과 대응하는 출력 이미지의 네 점이 필요하다.
#openCV에서는 두 이미지 간에 대응하는 네 점을 안다면 getAffineTransform 함수를 사용해 퍼스펙티브 변환 행렬을 얻을 수 있다.
#warpAffin 함수를 사용해 이미지에 적용한다.

#마우스 클릭을 해서 네 점을 지정한 후 스페이스바를 누르면 퍼스펙티브 변환이 적용된다.



import cv2 as cv
import numpy as np

#마우스 클릭한 좌표를 저장할 리스트이다.
src = np.zeros([4, 2], dtype=np.float32) #4행 2열의 행렬, 자료는 32비트 실수
idx = 0

def mouse_callback(event, x, y, flags, param):
    global point_list, idx

    #마우스 왼쪽 버튼을 누를 때마다 좌표를 리스트에 저장한다.
    if event == cv.EVENT_LBUTTONDOWN:

        src[idx] = (x,y)
        idx = idx + 1

        print("(%d , %d)" %(x,y))

        cv.circle(img_original, (x,y), 10, (0,0,255), -1)


#마우스 콜백함수를 등록한다.
cv.namedWindow('source')
cv.setMouseCallback('source', mouse_callback)

#사용할 이미지를 불러온다.
img_color = cv.imread('imgs/26437_83716_2610.jpg')
img_original = img_color.copy()

height, width = img_color.shape[:2]

#반복하면서 마우스 클릭으로 네 점을 지정하도록 한다.
while(True):

    cv.imshow('source', img_original)

    #space바를 누르면 루프에서 나온다.
    if cv.waitKey(1) == 32:
        break


#퍼스펙티브 변환 후 영역으로 사각영역을 지정한다.
dst = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

#퍼스펙티브 변환 행렬을 생성한다.
m = cv.getPerspectiveTransform(src, dst)

#이미지에 퍼스펙티브 변환 행렬을 적용한다.
img_result = cv.warpPerspective(img_original, m, (width, height))

#결과를 보여준다.
cv.imshow('result', img_result)
cv.waitKey(0)
cv.destroyAllWindows()