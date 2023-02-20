#필요한 OpenCV 패키지를 임포트합니다
import cv2

#첫 번째 아규먼트로(요소로) 지정한 파일을 컬러 포멧으로 불러옵니다.
#IMREAD_COLOR 는 컬러 포멧으로 이미지 파일을 읽겠다는 의미
#이미지를 img_color 변수에 넘파이 배열로 대입
img_color = cv2.imread("imgs/Screenshot_20220605-113327.png",cv2.IMREAD_COLOR)

#이미지를 불러올 수 없다면 img_color 변수는 None(값 없음) 이 됩니다
#이미지를 불러올 수 없는 경우를 체크합니다
if img_color is None:
    print("이미지를 읽어 올 수 없음. ")
    exit(1)

#이미지를 보여줄 윈도우를 생성합니다.
#첫번째 요소로 윈도우 식별자로 사용할 문자열을 지정해줍니다.
#지정한 문자열이 윈도우 타이틀바에 보입니다.
cv2.namedWindow('Color')


# 아래가 더 편하고 짧음(개인적 사견)
#윈도우 식별자가 "Color"인 윈도우에 변수 img_color 가 가리키는
#넘파이 배열에 저장된 이미지를 보여줍니다
#대부분의 경우 namedWindow 를 생략하고 imshow만 사용해도 윈도우에 이미지를 보여줍니다.
cv2.imshow('Color', img_color)

#ms 단위로 지정한 시간만큼 대기
#0 이라면 OpenCV로 생성한 윈도우 창이 생성된 상태에서 키보드 입력을 대기합니다.
cv2.waitKey(0)

#사용이 끝난 윈도우를 종료해줍니다.
cv2.destroyAllWindows()