# 얼굴 영역을 제외한 부분의 이미지 밝기 하향

from deepface import DeepFace
import cv2
import numpy as np

# 지정한 경로의 이미지에 나타난 얼굴을 분석하고 분석 내용 출력
face_analysis = DeepFace.analyze(img_path = "test1.jpg")
print(face_analysis)

# 분석한 얼굴 이미지 로드
img = cv2.imread("test2.jpg", cv2.IMREAD_COLOR)

# 얼굴 분석 내용 중 분석한 얼굴 영역 위치와 크기 정보 추출
region = face_analysis[0]['region']
# 얼굴 영역의 (좌상단 꼭짓점)위치 좌표 추출
pt1 = region['x'], region['y']
# 얼굴 영역의 좌상단 꼭짓점 위치와 높이 및 너비를 더하여 우하단 꼭짓점 위치 좌표 추출
pt2 = region['x'] + region['w'], region['y'] + region['h']
# 추출한 얼굴 영역을 별도 이미지로 저장
face = img[pt1[1]:pt2[1], pt1[0]:pt2[0]]

# 이미지를 32비트 정수형으로 변환
img = img.astype('int32')
# 이미지에서 밝기 수치를 최대 50 낮춤
img = np.clip(img - 50, 0, 255)
# 이미지를 부호없는 8비트 정수형으로 변환
img = img.astype('uint8')

# 밝기를 낮춘 이미지의 얼굴 위치에 밝기를 낮추지 않은 원본 얼굴 이미지를 덮어씌움
img[pt1[1]:pt2[1], pt1[0]:pt2[0]] = face

# 이미지에서 얼굴 영역의 좌상단 꼭짓점과 우하단 꼭짓점 좌표를 기준으로 직사각형 표시
cv2.rectangle(img, pt1=pt1, pt2=pt2, color=(241, 242, 64), thickness=1)
# 이미지를 창으로 출력
cv2.imshow("CIA", img)
# 아무 키 누르면 창 종료
cv2.waitKey(0)