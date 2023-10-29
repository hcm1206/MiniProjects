# 인식된 사람 얼굴 부분 모자이크

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

    # 얼굴 부분 영역을 저장
    face_region = img[startY:endY, startX:endX]
    # 얼굴 부분 영역의 원본 크기 저장
    M, N, D = face_region.shape

    # 얼굴 부분 영역을 0.05 비율로 크기 축소 조정 후 다시 원본 크기로 확대 조정하여 모자이크화
    face_region = cv2.resize(face_region, None, fx=0.05, fy=0.05, interpolation=cv2.INTER_AREA)
    face_region = cv2.resize(face_region, (N, M), interpolation=cv2.INTER_AREA)
    # 모자이크화된 얼굴 부분 영역을 원본 이미지에 적용
    img[startY:endY, startX:endX] = face_region

# 얼굴 부분이 모자이크된 이미지를 창으로 출력
cv2.imshow("detect and mosaic faces", img)
# 아무 키 누르면 창 종료
cv2.waitKey(0)
cv2.destroyAllWindows()
# 얼굴 부분이 모자이크된 이미지를 파일로 저장
cv2.imwrite('test_result.jpg', img)