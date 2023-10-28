# 명함 윤곽선을 잘라서 명함 부분만 출력

import cv2
import random
import numpy as np
import math

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
img_thresh = cv2.adaptiveThreshold(img_gray, maxValue=255.0, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    thresholdType=cv2.THRESH_BINARY_INV, blockSize=19, C=9)

# 이진 이미지 창으로 출력
cv2.imshow("test", img_thresh)
# 아무 키 누르면 창 종료
cv2.waitKey(0)

# 이진 이미지에서 윤곽선 탐색
contours, _ = cv2.findContours(img_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# 원본 이미지의 복사본 1 저장
img1 = img.copy()

# 복사본 이미지 1에서 각 윤곽선 부분을 랜덤한 색으로 표시
for i in range(len(contours)):
    cv2.drawContours(img1, contours[i], -1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 2)

# 윤곽선을 색으로 표시한 이미지 1 창으로 출력
cv2.imshow("test", img1)
# 아무 키 누르면 창 종료
cv2.waitKey(0)

# 원본 이미지의 복사본 이미지 2 저장
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
            cv2.rectangle(img_black1, pt1=(x, y), pt2=(x+w, y+h),
            color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=1)
            # 해당 바운딩 박스의 윤곽선과 위치, 크기 정보를 딕셔너리 형태로 리스트에 저장
            candidates.append({'contour': contour, 'x':x, 'y':y, 'w':w, 'h':h})

# 원본 이미지의 절반 이상 크기를 가진 바운딩 박스를 표시한 검은 배경 이미지를 창으로 출력
cv2.imshow("test", img_black)
# 아무 키 누르면 창 종료
cv2.waitKey(0)
# 원본 이미지의 절반 이상 크기를 가지고 너비와 높이 비율이 1:1에서 1:2 사이인 바운딩 박스를 표시한 검은 배경 이미지 복사본 1을 창으로 출력
cv2.imshow("test", img_black1)
# 아무 키 누르면 창 종료
cv2.waitKey(0)

# 바운딩 박스들의 넓이를 저장할 빈 리스트 생성
area_list = []

# 후보 바운딩 박스가 2개 이상이면
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
                pt2=(business_card['x']+business_card['w'], business_card['y']+business_card['h']), 
                color=(0, 0, 255), thickness=2)
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

# 명함 윤곽 중 x축 최소값 변수 생성(초기값 원본 이미지의 x축 최대값)
x_min = width
# 명함 윤곽 중 x축 최대값 변수 생성(초기값 0)
x_max = 0
# 명함 윤곽 중 y축 최소값 변수 생성(초기값 원본 이미지의 y축 최대값)
y_min = height
# 명함 윤곽 중 y축 최대값 변수 생성(초기값 0)
y_max = 0

# 명함 윤곽을 이루는 점들에 대하여 반복
for point in business_card['contour']:
    # 해당 점의 x축 좌표가 현재 x축 최소값 미만이라면
    if point[0][0] < x_min:
        # x축 최소값을 해당 점의 x축 좌표로 설정
        x_min = point[0][0]
        # x축 최소값에 대응하는 y축 좌표값을 해당 점의 y축으로 설정
        x_min_partner = point[0][1]
    # 해당 점의 x축 좌표가 현재 x축 최대값 미만이라면
    if point[0][0] > x_max:
        # x축 최대값을 해당 점의 x축 좌표로 설정
        x_max = point[0][0]
        # x축 최대값에 대응하는 y축 좌표값을 해당 점의 y축으로 설정
        x_max_partner = point[0][1]
    # 해당 점의 y축 좌표가 현재 y축 최소값 미만이라면
    if point[0][1] < y_min:
        # y축 최소값을 해당 점의 y축 좌표로 설정
        y_min = point[0][1]
        # y축 최소값에 대응하는 x축 좌표값을 해당 점의 x축으로 설정
        y_min_partner = point[0][0]
    # 해당 점의 y축 좌표가 현재 y축 최대값 미만이라면
    if point[0][1] > y_max:
        # y축 최대값을 해당 점의 y축 좌표로 설정
        y_max = point[0][1]
        # y축 최대값에 대응하는 x축 좌표값을 해당 점의 x축으로 설정
        y_max_partner = point[0][0]

# x축 최소값을 갖는 점1의 좌표 저장
pt1 = (x_min, x_min_partner)
# y축 최소값을 갖는 점2의 좌표 저장
pt2 = (y_min_partner, y_min)
# x축 최대값을 갖는 점3의 좌표 저장
pt3 = (y_max_partner, y_max)
# y축 최소값을 갖는 점4의 좌표 저장
pt4 = (x_max, x_max_partner)

# x축 최소값, 최대값과 y축 최소값, 최대값을 각각 갖는 점들의 좌표 출력
print(pt1, pt2, pt3, pt4)

# 원본 이미지에 x축 최소값을 갖는 점1의 위치 표시
cv2.circle(img, pt1, radius=5, color=(0, 0, 255), thickness=-1)
# 원본 이미지에 y축 최소값을 갖는 점2의 위치 표시
cv2.circle(img, pt2, radius=5, color=(0, 0, 255), thickness=-1)
# 원본 이미지에 x축 최대값을 갖는 점3의 위치 표시
cv2.circle(img, pt3, radius=5, color=(0, 0, 255), thickness=-1)
# 원본 이미지에 y축 최대값을 갖는 점4의 위치 표시
cv2.circle(img, pt4, radius=5, color=(0, 0, 255), thickness=-1)

# 명함 윤곽중 x축 최소값, x축 최대값, y축 최소값, y축 최대값을 각각 나타내는 점이 표시된 원본 이미지 창으로 출력
cv2.imshow("test", img)
# 아무 키 누르면 창 종료
cv2.waitKey(0)
# 점1, 점2의 거리와 점3, 점4의 거리 평균을 구하여 명함을 정렬(퍼스펙티브 변환)하여 출력하기 위한 너비 계산
new_width = int((math.dist(pt1, pt2) + math.dist(pt3, pt4))/2)
# 점2, 점4의 거리와 점1, 점3의 거리 평균을 구하여 명함을 정렬(퍼스펙티브 변환)하여 출력하기 위한 높이 계산
new_height = int((math.dist(pt2, pt4) + math.dist(pt1, pt3))/2)

# 명함 이미지에 퍼스펙티브 변환을 하기 위한 기준 꼭짓점 정보 설정
src = np.float32([list(pt1), list(pt2), list(pt3), list(pt4)])
# 명함 이미지에 퍼스펙티브 변환을 하기 위한 변환 후의 너비와 높이 정보 설정
dst = np.float32([[0, 0], [new_width, 0], [0, new_height], [new_width, new_height]])

# 설정을 토대로 명함 이미지 퍼스펙티브 변환
mat = cv2.getPerspectiveTransform(src, dst)

# 퍼스펙티브 변환한 이미지를 크기에 맞게 잘라내어 별도 이미지로 저장
img_card = cv2.warpPerspective(img, mat, (new_width, new_height))

# 퍼스펙티브 변환한 이미지의 높이가 너비보다 크다면 반시계방향으로 90도 회전
if new_width < new_height:
    img_card = cv2.rotate(img_card, cv2.ROTATE_90_COUNTERCLOCKWISE)

# 명함 부분만 추출된 최종 이미지를 창으로 출력
cv2.imshow("test", img_card)
# 아무 키 누르면 창 종료
cv2.waitKey(0)

# 명함 부분만 추출된 최종 이미지를 파일로 저장
cv2.imwrite("business_card.jpg", img_card)