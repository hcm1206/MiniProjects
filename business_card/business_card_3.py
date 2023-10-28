# 명함 바운딩 박스와 명함의 윤곽 추출

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

# 윤곽선을 색으로 표시한 이미지 1 창으로 출력
cv2.imshow("test", img1)
# 아무 키 누르면 창 종료
cv2.waitKey(0)

# 원본 이미지의 복사본 2 저장
img2 = img.copy()
# 원본 이미지와 동일한 크기의 검은 배경 이미지(넘파이 배열) 생성
img_black = np.zeros((width, height, colors), dtype=np.uint8)
# 검은 배경 이미지 복사본 1 저장
img_black1 = img_black.copy()

# 후보 바운딩 박스의 정보를 저장할 빈 리스트 생성
candidates = []

# 각 윤곽선 별로 반복
for contour in contours:
    # 각 윤곽선을 구성하는 위치와 크기 정보(바운딩 박스) 저장
    x, y, w, h = cv2.boundingRect(contour)

    # 바운딩 박스의 너비 또는 높이가 원본 이미지의 너비 또는 높이 절반보다 크면 검은 배경 이미지에 해당 바운딩 박스를 랜덤한 색으로 표시
    if w >= width/2 or h >= height/2:
        cv2.rectangle(img_black, pt1=(x,y), pt2=(x+w, y+h), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=1)

        # 해당 바운딩 박스의 너비/높이 또는 높이/너비 비율이 1:1에서 1:2 사이라면 검은 배경 이미지 복사본 1에 해당 바운딩 박스를 랜덤한 색으로 표시
        if (1 < w/h < 2) or (1 < h/w < 2):
            cv2.rectangle(img_black1, pt1=(x,y), pt2=(x+w, y+h), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=1)
            # 해당 바운딩 박스의 윤곽선과 위치, 크기 정보를 딕셔너리 형태로 리스트에 저장
            candidates.append({'contour': contour, 'x':x, 'y':y, 'w':w, 'h':h})

# 원본 이미지의 절반 이상 크기를 가진 바운딩 박스를 표시한 검은 배경 이미지를 창으로 출력
cv2.imshow("test", img_black1)
# 아무 키 누르면 종료
cv2.waitKey(0)

# 원본 이미지의 절반 이상 크기를 가지고 너비와 높이 비율이 1:1에서 1:2 사이인 바운딩 박스를 표시한 검은 배경 이미지 복사본 1을 창으로 출력
cv2.imshow("test", img_black1)
# 아무 키 누르면 종료
cv2.waitKey(0)

# 바운딩 박스들의 넓이를 저장할 빈 리스트 생성
area_list = []

# 후보 바운딩 박스가 2개 이상이라면
if len(candidates) >= 2:
    # 각 후보 바운딩 박스 별로 반복
    for candidate in candidates:
        # 해당 후보 바운딩 박스의 넓이 계산
        area = candidate['w'] * candidate['h']
        # 바운딩 박스 넓이를 리스트에 저장
        area_list.append(area)

    # 바운딩 박스 넓이들 중 최소 넓이를 추출
    min_area = min(area_list)
    # 최소 넓이를 가진 바운딩 박스 리스트 인덱스를 추출
    min_index = area_list.index(min_area)
    # 바운딩 박스 중 최소 넓이와 그 인덱스 출력
    print(min_area, min_index)
# 후보 바운딩 박스가 하나라면 해당 바운딩 박스 넓이를 최소 넓이로 설정
else:
    min_index = 0

# 최소 넓이를 가진 바운딩 박스를 명함 바운딩 박스라고 결정
business_card = candidates[min_index]

# 원본 이미지의 복사본 3 저장
img3 = img.copy()

# 복사본 이미지 3에서 명함 바운딩 박스를 직사각형으로 표시
cv2.rectangle(img3, pt1=(business_card['x'], business_card['y']), 
                pt2=(business_card['x']+business_card['w'], business_card['y']+business_card['h']), color=(0, 0, 255), thickness=2)
# 원본 이미지에 명함 바운딩 박스 내부의 윤곽을 표시
cv2.drawContours(img, business_card['contour'], -1, (255, 0, 0), 2)

# 명함 바운딩 박스가 표시된 복사본 이미지 3 창으로 출력
cv2.imshow("test", img3)
# 아무 키 누르면 창 종료
cv2.waitKey(0)

# 명함 바운딩 박스 내부의 윤곽 창으로 출력
cv2.imshow("test", img)
# 아무 키 누르면 창 종료
cv2.waitKey(0)