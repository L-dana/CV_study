import cv2

#컬러 이미지로 파일을 읽어옵니다.
img_color = cv2.imread("imgs/Screenshot_20220617-191333.png", cv2.IMREAD_COLOR)

if img_color is None:
    print("파일을 읽을 수 없습니다.")
    exit(1)

#컬러 이미지를 먼저 화면에 보여주고
cv2.namedWindow('Color')
cv2.imshow('Color',img_color)

#대기하다가 키보드 입력이 있을 시 아랫줄을 실행합니다.
cv2.waitKey(0)


#img_color 에 저장된 컬러 이미지를 그레이 스케일 이미지로 변환 후 img_gray에 저장합니다.
#COLOR_BGR2GRAY 는 RGB 채널을 가진 컬러 이미지를 그레이 스케일로 변환하겠다는 의미
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

#namedWindow 함수는 생략 가능
#img_gray에 저장된 그레이 스케일 이미지를 식별자가 "Grayscale" 인 창에 보여줍니다.
#첫 번째 요소를 앞에서 컬러이미지를 보여줄 때 사용한 'color'를 사용하도록 수정하면 
#그레이 스케일 이미지가 'color' 창에 보이게 됩니다.
cv2.imshow('Grayscale', img_gray)

#img_gray 에 저장된  이미지를 첫 번째 요소로 지정한 파일명으로 저장합니다.
#이미지 포멧은 지정한 확장자에 따릅니다.
cv2.imwrite("miku.png", img_gray)

#아무 키나 누르면 프로그램을 종료합니다.
cv2.waitKey(0)
cv2.destroyAllWindows()