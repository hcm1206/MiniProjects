# mnist 데이터셋 이미지 확인

import tensorflow as tf
import cv2

# mnist 데이터셋 로드
mnist = tf.keras.datasets.mnist
# mnist 데이터셋에서 훈련용 데이터와 시험용 데이터 추출
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 훈련용 데이터의 0번, 1번 인덱스 이미지 데이터를 각각 img1, img2로 저장
img1 = X_train[0]
img2 = X_train[1]

# img1, img2 이미지 데이터의 크기를 10배 확대 조정
img1_enlarged = cv2.resize(img1, None, fx=10, fy=10, interpolation=cv2.INTER_CUBIC)
img2_enlarged = cv2.resize(img2, None, fx=10, fy=10, interpolation=cv2.INTER_CUBIC)

# 확대된 img1 이미지 데이터를 창으로 출력
cv2.imshow('sample', img1_enlarged)
# 아무 키 누르면 창 종료
cv2.waitKey(0)

# 확대된 img2 이미지 데이터를 창으로 출력
cv2.imshow('sample', img2_enlarged)
# 아무 키 누르면 창 종료
cv2.waitKey(0)

# 훈련용 데이터의 0번, 1번 인덱스에 해당하는 라벨(숫자)을 추출하여 출력
label1 = y_train[0]
label2 = y_train[1]
print(label1, label2)