# 손글씨 전화번호 인식

import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# 학습된 딥러닝 모델 로드
model = load_model('model.h5')

# 손글씨 전화번호 이미지를 흑백으로 로드
img = cv2.imread('test1.png', cv2.IMREAD_GRAYSCALE)
# 이미지를 창으로 출력
cv2.imshow("test", img)
# 아무 키 누르면 창 종료
cv2.waitKey(0)

# 이미지 복사본 1 생성
img1 = img.copy()
# 이미지 복사본 1을 이진(black & white) 이미지 형태로 변환
_, img1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY_INV)
# 흑백 복사본 이미지 1에서 개체의 윤곽선 검출
contours, _ = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 이미지 복사본 2 생성
img2 = img.copy()

# 이미지 복사본 1에서 추출한 윤곽선 별로 반복
for i in range(len(contours)):
    # 이미지 복사본 2에 각 윤곽선을 표시
    cv2.drawContours(img2, contours[i], -1, (128,0,0), 2)

# 윤곽선이 표시된 이미지 창으로 출력
cv2.imshow("test", img2)
# 아무 키 누르면 창 종료
cv2.waitKey(0)

# 이미지 복사본 3 생성
img3 = img.copy()
# 숫자 후보 영역을 저장할 빈 리스트 생성
num_candidates = []

# 각 윤곽선 별로 반복
for contour in contours:
    # 윤곽선을 포함하는 사각형의 각 꼭짓점 좌표 추출
    x,y,w,h = cv2.boundingRect(contour)
    # 숫자 후보 영역 리스트에 윤곽선들의 각 꼭짓점 좌표 추가
    num_candidates.append((x,y,w,h))
    # 이미지 복사본 3에 해당 윤곽선 꼭짓점을 기준으로 사각형 표시
    cv2.rectangle(img3, pt1=(x,y), pt2=(x+w, y+h), color=(0,0,0), thickness=1)

# 숫자 윤곽선을 둘러싸는 사각형을 표시한 이미지 창으로 출력
cv2.imshow("test", img3)
# 아무 키 누르면 창 종료
cv2.waitKey(0)

# 숫자 윤곽선을 왼쪽 좌표에 가까운 순으로 정렬
num_candidates = sorted(num_candidates)
# 하이픈(-)을 제외하고 숫자의 윤곽선 좌표를 저장할 빈 리스트 생성
num_candidates1 = []

# 숫자 후보 리스트들의 숫자 후보 윤곽선 좌표별로 반복
for candidate in num_candidates:
    w,h = candidate[2], candidate[3]
    # 높이/너비 비율이 0.5보다 크고 너비와 높이가 3보다 크다면 숫자로 인식하여 숫자 윤곽선 좌표 리스트에 추가
    if h/w > 0.5 and w > 3 and h > 3:
        num_candidates1.append(candidate)

# 실제 숫자 저장할 빈 리스트 생성
phone_num = []

# 숫자로 판정된 후보군이 11개라면
if len(num_candidates1) == 11:
    # 각 숫자 윤곽선 좌표별로 반복
    for candidate in num_candidates1:
        # 숫자 윤곽선의 꼭짓점 좌표 추출
        x,y,w,h = candidate[0],candidate[1],candidate[2],candidate[3]
        # 전화번호 이미지에서 해당 부분의 숫자 영역만 이미지로 추출
        img_num = img[y:y+h, x:x+w]

        # 현재 숫자 영역 이미지를 이진(black & white) 이미지 형태로 변환
        _, img_num = cv2.threshold(img_num, 127, 255, cv2.THRESH_BINARY_INV)
        # 숫자 영역 이미지에서 높이와 너비 중 큰 값의 1/4을 마진으로 설정
        margin = int(max(w, h) / 4)
        # 숫자 영역 이미지 크기에 마진을 추가한 크기만큼의 배열 생성
        img_black = np.zeros((h+2*margin, w+2*margin), dtype=np.uint8)
        # 배열에 마진부분을 제외하고 숫자 영역 이미지를 저장(이미지 배열화)
        img_black[margin:margin+h, margin:margin+w] = img_num
        # 이미지 배열을 28 × 28 크기로 조정
        img_black = cv2.resize(img_black, (28, 28), interpolation=cv2.INTER_AREA)

        # 크기가 조정된 이미지를 창으로 출력
        cv2.imshow("test", img_black)
        # 아무 키 누르면 창 종료
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # 이미지 배열을 0~1 사이 값으로 정규화
        x = img_to_array(img_black)/255.0
        # 모델 입력값에 맞게 이미지 배열에 차원 추가하여 전처리
        x = np.expand_dims(x[:,:,0], axis=0)

        # 딥러닝 모델에 전처리된 이미지 입력하여 숫자값 예측
        prediction = model.predict(x)
        # 예측된 숫자값을 실제 숫자 리스트에 저장 -
        phone_num.append(np.argmax(prediction))
# 숫자로 판정된 후보군이 11개가 아니라면 예외 발생 후 종료
else:
    raise Exception("전화번호 11자리를 제대로 찾아내지 못했습니다.")

# 검출한 최종 전화번호 숫자 리스트 출력
print(phone_num)

# 전화번호 숫자 리스트의 값들을 문자열로 변환 후 출력
phone_num_str = [str(num) for num in phone_num]
print(f"검출된 전화번호: {''.join(phone_num_str)}")