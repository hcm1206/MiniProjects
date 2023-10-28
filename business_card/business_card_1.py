# 영상처리를 위한 명함 이미지 전처리 작업

import cv2
import random
import numpy as np

# 명함 원본 이미지 로드
img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
# 이미지 크기와 색 정보 추출
width, height, colors = img.shape
# 이미지 크기와 색 정보 출력
print(width, height, colors)

# 이미지 너비나 높이가 1000 이상이면 이미지를 20% 비율로 축소시킨 후 이미지 크기와 색 정보 재출력
if width > 1000 or height > 1000:
    img = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
    width, height, colors = img.shape
    print(width, height, colors)

# 이미지 색을 흑백으로 변환
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 흑백 이미지 창으로 출력
cv2.imshow("test", img_gray)
# 아무 키 누르면 창 종료
cv2.waitKey(0)

# 흑백 이미지를 이진(검정 or 하양) 이미지로 변환
img_thresh = cv2.adaptiveThreshold(img_gray, maxValue=255.0, 
                                    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                    thresholdType=cv2.THRESH_BINARY_INV, 
                                    blockSize=19, C=9)

# 이진 이미지 창으로 출력
cv2.imshow("test", img_thresh)
# 아무 키 누르면 창 종료
cv2.waitKey(0)

# 이진 이미지에서 윤곽선 탐색
contours, _ = cv2.findContours(img_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# 원본 이미지의 복사본 1 저장
img1 = img.copy()

# 복사본 이미지 1에서 각 윤곽선 부분을 색으로 표시
for i in range(len(contours)):
    cv2.drawContours(img1, contours[i], -1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 2)

# 윤곽선을 색으로 표시한 이미지를 창으로 출력
cv2.imshow("test", img1)
# 아무 키 누르면 창 종료
cv2.waitKey(0)

# 원본 이미지의 복사본 2 저장
img2 = img.copy()
# 원본 이미지와 동일한 크기의 검은 배경 이미지(넘파이 배열) 생성
img_black = np.zeros((width, height, colors), dtype=np.uint8)

# 각 윤곽선 별로 반복
for contour in contours:
    # 각 윤곽선을 구성하는 위치와 크기 정보(바운딩 박스) 추출
    x, y, w, h = cv2.boundingRect(contour)
    # 복사본 이미지 2에서 각 윤곽선의 바운딩 박스를 랜덤한 색으로 표시
    cv2.rectangle(img2, pt1=(x,y), pt2=(x+w, y+h), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=1)
    # 검은 배경 이미지에서 각 윤곽선의 바운딩 박스를 랜덤한 색으로 표시
    cv2.rectangle(img_black, pt1=(x,y), pt2=(x+w, y+h), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=1)

# 바운딩 박스를 표시한 복사본 이미지 출력
cv2.imshow("test", img2)
# 아무 키 누르면 창 종료
cv2.waitKey(0)

# 바운딩 박스를 표시한 검은 배경 이미지 출력
cv2.imshow("test", img_black)
# 아무 키 누르면 창 종료
cv2.waitKey(0)