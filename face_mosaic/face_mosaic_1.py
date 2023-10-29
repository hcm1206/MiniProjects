# 이미지에서 사람 얼굴 인식

import cvlib
import cv2

# 이미지 원본 로드
img = cv2.imread('test.jpg')

# 이미지에서 사람 얼굴을 인식하여 검출
faces, confidence = cvlib.detect_face(img)

# 검출된 얼굴 별로 반복
for face in faces:
    # 사람 얼굴로 인식된 영역의 좌상단 꼭짓점과 우하단 꼭짓점 좌표를 추출
    (startX, startY) = face[0], face[1]
    (endX, endY) = face[2], face[3]

    # 이미지에 사람 얼굴로 인식된 영역을 직사각형으로 표시
    cv2.rectangle(img, (startX, startY), (endX, endY), (0,255,0), 2)

# 사람 얼굴을 표시한 이미지를 창으로 출력
cv2.imshow("detect faces", img)
# 아무 키 누르면 창 종료
cv2.waitKey(0)
cv2.destroyAllWindows()