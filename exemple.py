import cv2

img_color = cv2.imread("imgs/Screenshot_20220605-113327.png", cv2.IMREAD_COLOR)

if img_color is None:
    print("이미지 파일을 읽을 수 없다.")
    exit(1)

cv2.namedWindow('cc')
cv2.imshow('cc', img_color)


cv2.waitKey(0)
cv2.destroyAllWindows()