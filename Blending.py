#블렌딩(blending) 은 2개의 입력 이미지의 투명도를 조정하여 2개의 이미지가 겹쳐보이게 하는 것이다.
#openCV 는 블렌딩을 위해 addWeighted 함수를 제공한다. 다음과 같이 작동한다.

# dst = src1 * alpha + src2 * beta + gamma
# 결과 = 이미지1 * 가중치1 + 이미지2 * 가중치2 + 추가 상수

#상수 alpha와 beta 를 가중치로 사용해 입력 이미지 src1, src2 의 투명도를 조절한다
# 상수가 가질 수 있는 범위는 0.0 ~ 1.0 이며 0.0에 가까울 수록 투명해진다.
# gamma는 가중치 합에 추가로 더하는 상수이다.

#첫번째 이미지를 위한 가중치 alpha는 점점 증가시키고, 두번째 이미지를 위한 가중치 beta는 점점 감소시킨다.
#실행 후 키보드의 아무 키나 누르면 점점 첫번째 사진이 사라지고 두번째 사진이 나타난다.



import cv2 as cv

alpha = 0.0
beta = 1.0

while alpha <= 1.0:
    #addWeighted 함수의 파라미터 조정 혀과를 확인하기 위해
    #루프 시작 때마다 이미지를 새로 불러온다.
    #블렌딩하는 두 이미지의 크기는 같아야 한다.
    img1 = cv.imread('imgs/Screenshot_20220617-191333.png',cv.IMREAD_COLOR)
    img2 = cv.imread('imgs/Screenshot_20220605-113327.png',cv.IMREAD_COLOR)

    #addWeightes 함수를 사용하여 블렌딩을 적용한다.
    #addWeighted(이미지1, 첫 가중치, 이미지2, 둘째 가중치, 감마(추가상수))
    dst = cv.addWeighted(img1, alpha, img2, beta, 0)

    #블렌딩을 위해 사용한 파라미터를 확인한다.
    print(alpha, " / ", beta)

    #결과 이미지를 화면에 보여준다.
    cv.imshow('dst', dst)
    cv.waitKey(0)

    #img1 을 위한 가중치 alpha는 0.1씩 증가시킴
    #img2 를 위한 가중치 beta는 0.1씩 감소시킴
    #img1 은 점점 불투명해지고 img2는 점점 투명해짐
    alpha = round(alpha + 0.1, 1)
    beta = round(beta - 0.1, 1)

#round()  반올림 함수
#round(숫자,정밀도)
#숫자 인자로 반올림 하고 싶은 숫자를 넣는다(숫자가 아닐 경우에는 None 반환.)
#정밀도 인자로 정수를 집어 넣는다. (2를 넣을 경우 소숫점 둘째 자리까지 반올림)
#정밀도를 생략할 경우 가장 가까운 정수 반환.


cv.destroyAllWindows()