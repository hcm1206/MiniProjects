# 이미지 상에서 얼굴 크기에 따라 모자이크 여부 결정

import cvlib
import cv2

# 모자이크를 하지 않을 얼굴 개수 설정
N = 2

# 이미지 원본 로드
img = cv2.imread('test1.jpg')

# 이미지에서 사람 얼굴을 인식하여 검출
faces, confidence = cvlib.detect_face(img)
# 각 얼굴 부분의 면적을 저장할 빈 리스트 생성
faces_area = []

# 검출된 얼굴 별로 반복
for face in faces:
    # 사람 얼굴로 인식된 영역의 좌상단 우하단 꼭짓점 좌표를 추출
    (startX, startY) = face[0], face[1]
    (endX, endY) = face[2], face[3]
    
    # 추출된 얼굴 영역의 꼭짓점 좌표를 통해 얼굴 영역의 넓이 계산 후 리스트에 저장
    face_area = (endX-startX) * (endY - startY)
    faces_area.append(face_area)

# 검출된 얼굴 영역의 면적들을 출력
print(faces_area)

# 얼굴 영역의 면적들을 내림차순으로 정렬하여 출력
faces_area_sorted = sorted(faces_area, reverse=True)
print(faces_area_sorted)

# 얼굴 영역들 중 면적이 1번째로 큰 얼굴부터 N번재로 큰 얼굴까지 모자이크 처리 대상에서 제외
min_face_area = min(faces_area_sorted[0:N])
print("모자이크 처리 기준이 될 얼굴 사이즈:", min_face_area)

# 검출된 얼굴 별로 반복
for face in faces:
    # 사람 얼굴로 인식된 영역의 좌상단 우하단 꼭짓점 좌표를 추출
    (startX, startY) = face[0], face[1]
    (endX, endY) = face[2], face[3]

    # 추출된 얼굴 영역의 꼭짓점 좌표를 통해 얼굴 영역의 넓이 계산
    face_area = (endX - startX)*(endY - startY)

    # 계산된 현재 얼굴 영역 넓이가 모자이크 기준 넓이보다 작다면
    if face_area < min_face_area:
        # 현재 얼굴 영역 저장
        face_region = img[startY:endY, startX:endX]
        # 현재 얼굴 영역 원본 크기 저장
        M, N, D = face_region.shape

        # 얼굴 영역을 0.05 비율로 축소 조정 후 다시 원본 크기로 확대 조정하여 모자이크화
        face_region = cv2.resize(face_region, None, fx=0.05, fy=0.05, interpolation=cv2.INTER_AREA)
        face_region = cv2.resize(face_region, (N, M), interpolation=cv2.INTER_AREA)
        # 모자이크화된 얼굴 영역을 원본 이미지에 적용
        img[startY:endY, startX:endX] = face_region

# 기준점이 되는 얼굴 크기보다 작은 얼굴 부분을 모자이크화한 이미지를 창으로 출력
cv2.imshow("detect and mosaic stranger faces", img)
# 아무 키 누르면 창 종료
cv2.waitKey(0)
cv2.destroyAllWindows()
# 기준점이 되는 얼굴 크기보다 작은 얼굴 부분을 모자이크화한 이미지를 파일로 저장
cv2.imwrite('test1_result.jpg', img)