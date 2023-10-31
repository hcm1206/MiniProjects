# 직접 쓴 글자 이미지 모델에 인식

import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# 학습된 딥러닝 모델 로드
model = load_model('model.h5')

# 직접 쓴 글자 이미지를 흑백 이미지로 로드
img = cv2.imread('1.png', cv2.IMREAD_GRAYSCALE)
# 글자 이미지 창으로 출력
cv2.imshow("test", img)
# 아무 키 누르면 창 종료
cv2.waitKey(0)

# 이미지를 이진(black & white) 이미지 형태로 변환
_, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# 이미지 크기를 28 × 28 크기로 조정
img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
# 이미지 데이터를 0~1 사이 갑승로 정규화하여 배열로 저장
x = img_to_array(img)/255.0
# 이미지 배열 데이터에 차원을 추가하여 모델 입력값으로 전처리
x = np.expand_dims(x[:,:,0], axis=0)

# 전처리된 이미지 배열을 딥러닝 모델에 입력하여 숫자값 예측 후 출력
prediction = model.predict(x)
print(f"예측된 숫자: {np.argmax(prediction)}")