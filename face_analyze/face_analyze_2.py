# 얼굴 이미지의 분석 내용 출력 및 분석한 얼굴 부분을 이미지에서 사각형으로 표시

from deepface import DeepFace
import cv2

# 지정한 경로의 이미지에 나타난 얼굴을 분석하고 분석 내용 출력
face_analysis = DeepFace.analyze(img_path = "test1.jpg")
print(face_analysis)

# 분석한 얼굴 이미지 로드
img = cv2.imread("test1.jpg", cv2.IMREAD_COLOR)

# 얼굴 분석 내용 중 분석한 얼굴 영역 위치와 크기 정보 추출
region = face_analysis[0]['region']
# 얼굴 영역의 (좌상단 꼭짓점)위치 좌표 추출
pt1 = region['x'], region['y']
# 얼굴 영역의 좌상단 꼭짓점 위치와 높이 및 너비를 더하여 우하단 꼭짓점 위치 좌표 추출
pt2 = region['x'] + region['w'], region['y'] + region['h']

# 얼굴 이미지에 좌상단 꼭짓점과 우하단 꼭짓점 좌표를 기준으로 직사각형 표시
cv2.rectangle(img, pt1=pt1, pt2=pt2, color=(241, 242, 64), thickness=1)
# 이미지를 창으로 출력
cv2.imshow("CIA", img)
# 아무 키 누르면 창 종료
cv2.waitKey(0)