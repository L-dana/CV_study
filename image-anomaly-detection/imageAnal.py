import cv2 as cv
import numpy as np

#이미지 픽셀 분석

"""
1. 채널별로 분류 (RGB)
2. 채널마다 픽셀값을 조사 (픽셀값은 0~ 255 인데 맨 앞 자리 수 0~9 값의 비중을 조사)
3. RGB채널별로 조사한 픽셀값 비중을 출력

>> 함수의 리턴 = 이미지 픽셀값을 십진수로 계산했을 때 맨 앞자리 수의 비중
(0~9) 가 각각 몇개인지. 

4. 벤 포드 법칙에 따르는지 위배되는지? 고려해본다.


"""


#이미지를 불러온다.
src = cv.imread('image-anomaly-detection/train/stego/00001.png', cv.IMREAD_COLOR)

height, width = src.shape[:2]

#컬러 이미지를 BGR채널로 분리한다.
#bgr_channels = cv.split(src) # 0, 1, 2 -> blue, green, red

#10진수의 맨 앞자리 숫자 갯수를 센다
Pixel_front_value_b = [0,0,0,0,0,0,0,0,0,0] # 0~9 의 갯수 blue
Pixel_front_value_g = [0,0,0,0,0,0,0,0,0,0] # 0~9 의 갯수 green
Pixel_front_value_r = [0,0,0,0,0,0,0,0,0,0] # 0~9 의 갯수 red
Pixel_front_value_ALL = [0,0,0,0,0,0,0,0,0,0] # 0~9 의 갯수 ALL


#픽셀값 조사
for y in range (0,height):
    for x in range (0, width):
        b = src.item(y, x, 0)
        bs = "{}".format(b)
        Pixel_front_value_b[int(bs[0])] = Pixel_front_value_b[int(bs[0])] + 1

        g = src.item(y, x, 1)
        gs = "{}".format(g)
        Pixel_front_value_g[int(gs[0])] = Pixel_front_value_g[int(gs[0])] + 1

        r = src.item(y, x, 2)
        rs = "{}".format(r)
        Pixel_front_value_r[int(rs[0])] = Pixel_front_value_r[int(rs[0])] + 1

for i in range (0, 10):
    Pixel_front_value_ALL[i] = Pixel_front_value_b[i] + Pixel_front_value_g[i] + Pixel_front_value_r[i]

print(Pixel_front_value_ALL)
#print(type(src.item(1, 1,0)))

