#아핀 변환( Affine Transformation ) 은 세 점을 지정해서 세 점을 기준으로 이미지를 변형하는 변환이다.
#세 개의 좌표가 변한 수치만큼 이미지를 비틀어준다.

#아핀 변환을 위해서는 입력 이미지의 세 점과 대응하는 결과 이미지의 세 점이 필요하다.
#openCV 에서는 두 이미지 간에 대응하는 세 점을 안다면 getAffineTransform 함수를
#이용하여 아핀 변환 행렬을 얻을 수 있다. warpAfiine 함수를 사용해 이미지에 적용한다.

#마우스 클릭을 하여 세 점을 지정한 후 스페이스바를 누르면 아핀 변환이 적용된다.

# 점 두개를 고정적으로 쓰고 마지막 한 점의 위치변화를 이미지 전체가 공유하는 느낌이다.
# 점 두개를 찍고 나머지 점 하나의 위치를 바꾸면 그 위치를 이미지가 따라감 <<


from cv2 import waitKey
import numpy as np
import cv2 as cv

point_list = []

def mouse_callback(event, x, y, flags, param):
    #마우스 왼쪽 버튼을 누를 때마다 좌표를 리스트에 저장한다..
    if(event == cv.EVENT_LBUTTONDOWN):
        
        print(" (%d, %d)" %(x,y))

        point_list.append((x,y))
        cv.circle(img_color, (x,y), 3, (0,0,255), -1)


#마우스 콜백함수를 등록한다.
cv.namedWindow('source')
cv.setMouseCallback('source', mouse_callback)

#사용할 이미지를 불러온다.
img_color = cv.imread('imgs/roffjrtlvhfem.PNG', cv.IMREAD_COLOR)

#반복하며 마우스 클릭으로 세 점을 지정하게 한다.
while(True):
    cv.imshow('source', img_color)

    #space 바를 누르면 루프에서 나온다.
    if waitKey(1) == 32:
        break


height, weight = img_color.shape[:2]

#오른쪽 상단의 대응점만 y 좌표가 아래로 100 이동하도록 지정한다.
pts1 = np.float32([point_list[0], point_list[1], point_list[2]]) #처음 찍은 점들
pts2 = np.float32([point_list[0], point_list[1], point_list[2]]) #변형을 기록할 점들
pts2[1][1] += 100 #변형사항.( 오른쪽 상단 점(3번째)의 좌표를 아래로 100 만큼 내린다. )

#아핀 변환 행렬을 생성한다.
m = cv.getAffineTransform(pts1, pts2)

#이미지에 아핀 변환 행렬을 적용한다.
img_result = cv.warpAffine(img_color, m, (weight, height))

#결과를 보여준다.
cv.imshow('result', img_result)
cv.waitKey(0)

cv.destroyAllWindows()