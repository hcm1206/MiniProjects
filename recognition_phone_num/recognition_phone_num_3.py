import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense

# mnist 데이터셋 로드
mnist = tf.keras.datasets.mnist
# mnist 데이터셋에서 훈련용 데이터와 시험용 데이터 추출
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 0~255 사이의 색 정보를 나타내는 데이터 입력값을 0~1 사이의 값으로 정규화
X_train = X_train/255.0
X_test = X_test/255.0

# Sequential 딥러닝 모델 구성
model = Sequential([
    # 28 × 28 크기 입력값을 1차원으로 변환하는 Flatten 계층 구성
    Flatten(input_shape=(28, 28)),
    # 256개 노드로 이루어진 활성화 함수로 relu를 사용하는 Dense 계층(은닉층) 구성
    Dense(256, activation=tf.nn.relu),
    # 10개의 노드(0~9)로 이루어진 활성화 함수로 softmax를 사용하는 Dense 계층(출력층) 구성
    Dense(10, activation=tf.nn.softmax)
])

# 옵티마이저로 adam, 손실함수로 범주형 교차 엔트로피 오차 함수, 기준을 정확도로 하도록 모델을 컴파일하여 완성
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# 글씨를 잘 분류할 수 있도록 에폭을 10으로 설정하여 훈련용 데이터 학습
model.fit(X_train, y_train, epochs=20)
# 학습된 모델을 파일로 저장
model.save('model.h5')

# 테스트 데이터를 통해 모델의 정확도 측정 후 출력
_, accuracy = model.evaluate(X_test, y_test)
print(f"테스트 분류 정확도: {accuracy}")