# mnist 데이터셋의 데이터 체크

import tensorflow as tf

# mnist 데이터셋 로드
mnist = tf.keras.datasets.mnist
# mnist 데이터셋에서 훈련용 데이터와 시험용 데이터 추출
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# 훈련용 데이터의 데이터 행렬 형상과 개수 출력
print(X_train.shape, y_train.shape)
# 시험용 데이터의 데이터 행렬 형상과 개수 출력
print(X_test.shape, y_test.shape)