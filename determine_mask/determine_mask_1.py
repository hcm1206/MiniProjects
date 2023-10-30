# 마스크를 미착용한 얼굴 이미지 수집

import cv2
import cvlib as cv
import os
from datetime import datetime
from pytz import timezone

# nomask 디렉터리가 없으면 생성
try:
    os.makedirs('./nomask')
except FileExistsError:
    pass

# 컴퓨터의 웹캠을 인식 후 실행
webcam = cv2.VideoCapture(0)

# 웹캠을 열 수 없다면 오류 메시지 출력 후 프로그램 종료
if not webcam.isOpened():
    print("Could not open webcam")
    exit()

# 캡처한 이미지 수를 셀 변수 선언하여 0으로 초기화
sample_num = 0

# 웹캠이 열려 있다면 반복
while webcam.isOpened():
    # 웹캠을 통해 이미지 촬영
    status, frame = webcam.read()
    # 캡처한 이미지 수를 1 증가
    sample_num += 1

    # 웹캠 상태가 False라면 이미지 촬영 종료
    if not status:
        break
    
    # 매 8번째 이미지마다 아래 내용 실행
    if sample_num % 8 == 0:
        # 이미지로부터 얼굴 인식하여 추출
        face, confidence = cv.detect_face(frame)

        # 각 얼굴별로 반복
        for idx, f in enumerate(face):
            # 얼굴 영역의 좌측 상단 꼭짓점 좌표와 우측 하단 꼭짓점 좌표 추출
            (startX, startY) = f[0], f[1]
            (endX, endY) = f[2], f[3]
            # 추출한 꼭짓점 좌표를 통해 얼굴 영역을 별도의 이미지로 지정
            face_in_img = frame[startY:endY, startX:endX, :]

            # 현재 시간 확인
            now_time = datetime.now(timezone('Asia/Seoul')).strftime('%Y%m%d_%H%M%S%f')
            # 얼굴 이미지 캡쳐 여부를 현재 시간과 함께 출력
            print(f'{now_time}에 얼굴 이미지 캡처')
            # 캡처한 얼굴 이미지를 nomask 디렉터리에 저장
            cv2.imwrite('./nomask/face' + now_time + '.jpg', face_in_img)

        # 현재 캡쳐된 이미지 전체를 창으로 출력
        cv2.imshow("captured frames", frame)

        # 키보드 'q'를 누르면 캡쳐 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# 웹캠 사용 종료
webcam.release()
# 모든 창 종료
cv2.destroyAllWindows()