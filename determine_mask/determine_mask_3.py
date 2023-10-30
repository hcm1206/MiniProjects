# 수집된 이미지를 통해 마스크 착용 여부 판정하는 딥러닝 모델 구성

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten, BatchNormalization
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# 마스크 미착용 이미지가 저장된 디렉터리 경로 설정
path_dir1 = './nomask/'
# 마스크 착용 이미지가 저장된 디렉터리 경로 설정
path_dir2 = './mask/'
# 마스크 미착용 이미지 파일 저장
file_list1 = os.listdir(path_dir1)
# 마스크 착용 이미지 파일 저장
file_list2 = os.listdir(path_dir2)
# 마스크 미착용 이미지 파일 개수 저장
file_list1_num = len(file_list1)
# 마스크 착용 이미지 파일 개수 저장
file_list2_num = len(file_list2)
# 전체 이미지 파일 개수 계산
file_num = file_list1_num + file_list2_num

# 변환한 이미지 인덱스를 저장할 변수 선언하여 0으로 초기화
num = 0
# 이미지를 244 × 244 크기로 저장하기 위한 전체 이미지 파일 개수만큼의 배열 생성
all_img = np.float32(np.zeros((file_num, 224, 224, 3)))
# 이미지의 라벨(0 또는 1)을 저장하기 위한 전체 이미지 파일 개수만큼의 배열 생성
all_label = np.float64(np.zeros((file_num, 1)))

# 마스크 미착용 이미지들을 하나씩 반복
for img_name in file_list1:
    # 마스크 미착용 이미지 경로 설정
    img_path = path_dir1 + img_name
    # 마스크 미착용 이미지를 224 × 244 크기로 로드
    img = load_img(img_path, target_size=(224, 224))
    # 이미지를 배열로 변환
    x = img_to_array(img)
    # 배열로 변환된 이미지에 차원 추가
    x = np.expand_dims(x, axis=0)
    # 차원 추가된 이미지를 입력값으로 전처리
    x = preprocess_input(x)
    # 전처리된 이미지를 이미지 배열에 현재 인덱스로 저장
    all_img[num, :, :, :] = x
    # 마스크 미착용을 나타내는 값 0을 라벨 배열에 현재 인덱스로 저장
    all_label[num] = 0
    # 다음 인덱스로 1 추가
    num += 1

# 마스크 착용 이미지들을 하나씩 반복
for img_name in file_list2:
    # 마스크 착용 이미지 경로 설정
    img_path = path_dir2 + img_name
    # 마스크 미착용 이미지를 244 × 244 크기로 로드
    img = load_img(img_path, target_size=(224, 224))
    # 이미지를 배열로 변환
    x = img_to_array(img)
    # 배열로 변환된 이미지에 차원 추가
    x = np.expand_dims(x, axis=0)
    # 차원 추가된 이미지를 입력값으로 전처리
    x = preprocess_input(x)
    # 전처리된 이미지를 이미지 배열에 현재 인덱스로 저장
    all_img[num, :, :, :] = x
    # 마스크 미착용을 나타내는 값 1을 라벨 배열에 현재 인덱스로 저장
    all_label[num] = 1
    # 다음 인덱스로 1 추가
    num += 1

# 라벨로 저장된 값들의 개수(데이터 개수) 추출
n_elem = all_label.shape[0]
# 라벨 인덱스들을 랜덤으로 셔플
indices = np.random.choice(n_elem, size=n_elem, replace=False)
# 라벨 배열을 랜덤 셔플된 인덱스 기준으로 저장
all_label = all_label[indices]
# 이미지 배열을 랜덤 셔플된 인덱스 기준으로 저장
all_img = all_img[indices]
# 셔플된 인덱스 중 80%를 훈련 데이터 인덱스로 지정
num_train = int(np.round(all_label.shape[0]*0.8))
# 셔플된 인덱스 중 20%를 테스트 데이터 인덱스로 지정
num_test = int(np.round(all_label.shape[0]*0.2))
# 80% 인덱스까지의 이미지를 훈련 데이터 이미지로 지정
train_img = all_img[0:num_train, :, :, :]
# 나머지 20% 인덱스 이미지를 테스트 데이터 이미지로 지정
test_img = all_img[num_train:, :, :, :]
# 80% 인덱스까지의 라벨을 테스트 데이터 라벨로 지정
train_label = all_label[0:num_train]
# 나머지 20% 인덱스 이미지를 테스트 데이터 라벨로 지정
test_label = all_label[num_train:]

# 이미지 형상 설정
IMG_SHAPE = (224, 224, 3)
# 이미지넷 데이터셋에서 입력값을 설정한 이미지 형상 배열로하고 모델의 마지막 층을 제거
base_model = ResNet50(input_shape=IMG_SHAPE, weights='imagenet', include_top=False)
# 모델 훈련 여부를 False로 설정
base_model.trainable = False
# 모델 구조의 개요 출력
base_model.summary()
# 기본 이미지넷 모델의 계층 개수 출력
print("Number of layers in the base model: ", len(base_model.layers))

# Flatten 계층 객체 생성
flatten_layer = Flatten()
# 128개 노드로 이루어진 relu 활성화 함수를 사용하는 Dense 계층(은닉층) 객체 생성
dense_layer1 = Dense(128, activation='relu')
# BatchNormalization 계층 객체 생성
bn_layer1 = BatchNormalization()
# 1개 노드로 이루허진 sigmoid 활성화 함수를 사용하는 Dense 계층(출력층) 객체 생성
dense_layer2 = Dense(1, activation=tf.nn.sigmoid)

# 생성한 계층을 순차적으로 연결하여 Sequential 딥러닝 모델 객체 생성
model = Sequential([
    base_model,
    flatten_layer,
    dense_layer1,
    bn_layer1,
    dense_layer2,
])

# 초기 학습률을 0.001로 지정
base_learning_rate = 0.001
# 옵티마이저로 0.001 학습률의 Adam, 손실 함수로 이진 교차 엔트로피 오차 함수, 기준을 정확도로 하도록 모델을 컴파일하여 완성
model.compile(optimizer=tf.keras.optimizers.Adam(lr=base_learning_rate), loss='binary_crossentropy', metrics=['accuracy'])
# 완성된 모델의 개요 출력
model.summary()
# 마스크 얼굴 이미지를 잘 분류할 수 있도록 에폭을 10, 배치 크기를 16, 테스트 데이터를 통해 검증하며 모델 학습
model.fit(train_img, train_label, epochs=10, batch_size=16, validation_data = (test_img, test_label))

# 학습된 모델을 별도 파일로 저장
model.save("model.h5")
# 파일 저장 시 알림문 출력
print("Saved model to disk")