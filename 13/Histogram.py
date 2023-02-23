#히스토그램 Histogram 은 이미지를 구성하는 픽셀값 분포에 대한 그래프이다.
#x축은 픽셀값으로 0~255 의 범위를 가지고, y축은 해당 픽셀값을 가진 픽셀의 개수를 나타낸다.
#왼쪽은 가장 어두운 픽셀(0 = 검은색) 의 개수를 보여주며 오른쪽으로 갈수록 밝은 픽셀 수를 보여준다..

#히스토그램을 보면 이미지의 빛의 노출정도를 알 수 있다.
#어둡게 찍힌 이미지의 경우 히스토그램이 왼쪽에 몰려있게 된다. 
#조명이 알맞다면 히스토그램이 좌우로 골고루 퍼져있게 된다.

#히스토그램은 두 가지 파라미터를 고려한다.
#픽셀 강도 범위 - 히스토그램을 구할 때 사용할 값의 범위, 예시로 0~15로 결정하면
#0~15 범위의 픽셀값의 수를 구한다.

#막대의 범위 - 막대 하나로 보여줄 픽셀값의 범위.
#위에서 지정한 픽셀 강도 범위를 기준으로 막대가 보여줄 값의 범위를 4로 놓으면 막대가 4개 생기고
#각 막대는 0~3, 4~7 .... 의 4가지 픽셀값의 개수를 나타낸다.


#openCV에서는 히스토그램을 구하기 위해서 calcHist() 함수를 제공한다.
#hist = calcHist(입력 이미지, 채널의 인덱스, 마스크 이미지, 막대 수, 계산 범위, accumulate = False)
#hist - 히스토그램 계산 결과( Mat 자료형 )
#입력 이미지 - uint8 또는 float32 타입의 이미지에 대한 배열을 써야 한다.
#채널의 인덱스 - 히스토그램을 계산할 채널의 인덱스(RGB)/ 입력 이미지 배열에 포함된 이미지의 개수
#마스크 이미지 - 전체 이미지에 대한 히스토그램을 구할 거라면 None또는 Mat()를 사용해야 한다.
#				이미지 일부에 대한 히스토그램을 구하고자 한다면 마스크 이미지를 생성해서 제공해야 한다.
#막대 수(HistSize) - 계산할 히스토그램 막대(Bin) 의 개수
#계산 범위(ranges) - 히스토그램을 계산할 범위(최소값~최대값 = 0~256)
#accumulate -  히스토그램 막대 크기가 똑같고 처음 시작 시 히스토그램이 비어있도록 한다.


#컬러 이미지의 채널별 히스토그램 그리기.




import cv2 as cv
import numpy as np

#이미지를 불러온다.
src = cv.imread('imgs/20230223_185416044.jpg', cv.IMREAD_COLOR)

#컬러 이미지를 BGR채널로 분리한다.
bgr_channels = cv.split(src)

#픽셀값의 범위는 0~255 이므로 전체 막대 수는 256개.
histSize = 256

#픽셀값의 범위는 0~255이고, 상위 경계 256은 포함하지 않는다.
histRange = (0, 256)

#히스토그램 막대 크기가 똑같고 처음 시작 시 히스토그램이 비어있도록 한다.
accumulate = False


#BGR 채널별로 히스토그램을 계산한다.

#hist = calcHist(입력 이미지, 채널의 인덱스, 마스크 이미지, 막대 수, 계산 범위)
#hist - 히스토그램 계산 결과( Mat 자료형 )
#입력 이미지 - uint8 또는 float32 타입의 이미지에 대한 배열을 써야 한다.
#채널의 인덱스 - 히스토그램을 계산할 채널의 인덱스(RGB)/ 입력 이미지 배열에 포함된 이미지의 개수
#마스크 이미지 - 전체 이미지에 대한 히스토그램을 구할 거라면 None또는 Mat()를 사용해야 한다.
#				이미지 일부에 대한 히스토그램을 구하고자 한다면 마스크 이미지를 생성해서 제공해야 한다.
#막대 수(HistSize) - 계산할 히스토그램 막대(Bin) 의 개수
#계산 범위(ranges) - 히스토그램을 계산할 범위(최소값~최대값 = 0~256)
#accumulate -  히스토그램 막대 크기가 똑같고 처음 시작 시 히스토그램이 비어있도록 한다.
b_histogram = cv.calcHist(bgr_channels, [0], None, [histSize], histRange, accumulate=accumulate)
g_histogram = cv.calcHist(bgr_channels, [1], None, [histSize], histRange, accumulate=accumulate)
r_histogram = cv.calcHist(bgr_channels, [2], None, [histSize], histRange, accumulate=accumulate)

#히스토그램을 보여줄 이미지를 생성한다.
hist_w = 356*3
hist_h = 400
histimg = np.zeros((hist_h, hist_w,3), dtype=np.uint8)

#히스토그램을 정규화한다.
# ********** 책과는 사용방법이 다르다. 아마도 버전업을 하면서 사용법이 변한듯 함. 
bh = cv.normalize(b_histogram, None, 0, hist_h, cv.NORM_MINMAX)
gh = cv.normalize(g_histogram, None, 0, hist_h, cv.NORM_MINMAX)
rh = cv.normalize(r_histogram, None, 0, hist_h, cv.NORM_MINMAX)
#normalize(입력, 정규화 이후 데이터(출력), a, b, NORM_MINMAX)
#a - 정규화 구간1 (시작)
#b - 정규화 구간2 (끝)
	 
#NORM_MINMAX - 정규화 알고리즘 선택 플래그 상수
#a와 b 구간으로 정규화하는NORM_MINMAX
#전체 합으로 나누는 NORM_L1
#단위 벡터로 정규화하는 NORM_L2
#최댓값으로 나누는 NORM_INF


#히스토그램을 그려준다.
for i in range(0, histSize):

    #파란색 히스토그램
    cv.line(histimg, (i, hist_h - int(np.round(bh[i]))), (i, hist_h - 0), (255, 0, 0), thickness= 2)
    #초록색 히스토그램
    cv.line(histimg, (i + 256, hist_h - int(np.round(gh[i-1]))), (i + 256, hist_h - 0), (0, 255, 0), thickness= 2)
    #빨간색 히스토그램
    cv.line(histimg, (i + 256*2, hist_h - int(np.round(rh[i-2]))), (i + 256 * 2, hist_h - 0), (0, 0, 255), thickness= 2)


#결과 출력
cv.imshow('Source image', src)
cv.imshow('Histogram', histimg)
cv.waitKey(0)