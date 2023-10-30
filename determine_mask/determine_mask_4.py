import cvlib as cv
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array

# 학습된 딥러닝 모델 로드
model = load_model('model.h5')
# 모델 개요 출력
model.summary()

# 컴퓨터의 웹캠을 인식 후 실행
webcam = cv2.VideoCapture(0)

# 웹캠을 열 수 없다면 에러 메시지 출력 후 종료
if not webcam.isOpened():
    print("Could not open webcam")
    exit()

# 웹캠이 열려있다면 반복
while webcam.isOpened():
    # 웹캠을 통해 이미지 촬영
    status, frame = webcam.read()

    # 웹캠 상태가 False라면 프로그램 종료
    if not status:
        print("Could not read frame")
        exit()

    # 이미지로부터 얼굴 인식하여 추출
    face, confidence = cv.detect_face(frame)

    # 각 얼굴 별로 반복
    for idx, f in enumerate(face):
        # 얼굴 영역의 좌측 상단 꼭짓점 좌표와 우측 하단 꼭짓점 좌표 추출
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]

        # 이미지에서 얼굴 부분을 구분하는 꼭짓점 좌표를 통해 얼굴 영역을 별도의 이미지로 저장
        face_region = frame[startY:endY, startX:endX]
        # 추출한 얼굴 이미지를 224 × 224 크기로 조정
        face_region1 = cv2.resize(face_region, (224, 224), interpolation = cv2.INTER_AREA)

        # 얼굴 이미지를 배열로 변환
        x = img_to_array(face_region1)
        # 배열로 변환된 이미지에 차원 추가
        x = np.expand_dims(x, axis=0)
        # 차원 추가된 이미지를 입력값으로 전처리
        x = preprocess_input(x)

        # 전처리된 이미지를 딥러닝에 입력하여 예측값(마스크 착용 여부) 추측
        prediction = model.predict(x)

        # 예측된 마스크 착용 확률이 50% 미만이라면
        if prediction < 0.5:
            # 얼굴 부분에 붉은색으로 직사각형을 표시하고 직사각형 위에 No Mask 문구와 마스크를 착용하지 않았을 확률을 계산하여 표시
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
            Y = startY - 10 if startY - 10 > 10 else startY + 10
            text = "No Mask ({:.2f}%)".format((1 - prediction[0][0])*100)
            cv2.putText(frame, text, (startX, Y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
        # 예측한 마스크 착용 확률이 50% 이상이라면
        else:
            # 마스크를 착용한 얼굴 부분에 초록색으로 직사각형을 표시하고 직사각형 위에 Mask 문구와 마스크를 착용했을 확률을 계산하여 표시
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            Y = startY - 10 if startY - 10 > 10 else startY + 10
            text = "Mask ({:.2f}%)".format(prediction[0][0]*100)
            cv2.putText(frame, text, (startX, Y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
    
    # 현재 캡쳐된 이미지 전체를 창으로 출력
    cv2.imshow("mask or nomask", frame)

    # 키보드 'q'를 누르면 캡처 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠 사용 종료
webcam.release()
# 모든 창 종료
cv2.destroyAllWindows()