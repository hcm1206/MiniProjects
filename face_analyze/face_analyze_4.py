# 이미지에 얼굴 분석 정보 표시

from deepface import DeepFace
import cv2
import numpy as np

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
# 추출한 얼굴 영역을 별도 이미지로 저장
face = img[pt1[1]:pt2[1], pt1[0]:pt2[0]]

# 이미지를 32비트 정수형으로 변환
img = img.astype('int32')
# 이미지에서 밝기 수치를 최대 50 낮춤
img = np.clip(img - 50, 0, 255)
# 이미지를 부호없는 정수형 8비트로 전환
img = img.astype('uint8')

# 밝기를 낮춘 이미지의 얼굴 위치에 밝기를 낮추기 않은 원본 얼굴 이미지를 덮어씌움
img[pt1[1]:pt2[1], pt1[0]:pt2[0]] = face

# 이미지에서 얼굴 영역의 좌상단 꼭짓점과 우하단 꼭짓점 좌표를 기준으로 직사각형 표시
cv2.rectangle(img, pt1=pt1, pt2=pt2, color=(241, 242, 64), thickness=1)

# 얼굴 분석 내용 중 가장 확률이 높은 성별 추출
gender = face_analysis[0]['dominant_gender']
# 얼굴 분석 내용 중 추측된 나이 추출
age = str(face_analysis[0]['age'])
# 얼굴 분석 내용 중 가장 확률이 높은 인종 추출
race = face_analysis[0]['dominant_race']
# 얼굴 분석 내용 중 가장 확률이 높은 감정 추출
emotion = face_analysis[0]['dominant_emotion']
# 가장 확률이 높은 인종의 확률 추출
race_per = str(round(face_analysis[0]['race'][race], 1))
# 가장 확률이 높은 감정의 확률 추출
emotion_per = str(round(face_analysis[0]['emotion'][emotion], 1))

# 이미지에서 얼굴 영역 우측에 가장 확률이 높은 성별 표시
cv2.putText(img, 'Gender: ' + gender, (pt2[0]+10, pt1[1]+10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (241, 242, 64), 1, cv2.LINE_AA)
# 이미지에서 얼굴 영역 우측에 추측된 나이 표시
cv2.putText(img, 'Age: ' + age, (pt2[0]+10, pt1[1]+30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (241, 242, 64), 1, cv2.LINE_AA)
# 이미지에서 얼굴 영역 우측에 가장 확률이 높은 인종과 그 확률 표시
cv2.putText(img, 'Race: ' + race + ' ' + race_per + '%', (pt2[0]+10, pt1[1]+50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (241, 242, 64), 1, cv2.LINE_AA)
# 이미지에서 얼굴 영역 우측에 가장 확률이 높은 감정과 그 확률 표시
cv2.putText(img, 'Emotion ' + emotion + ' ' + emotion_per + '%', (pt2[0]+10, pt1[1]+70), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (241, 242, 64), 1, cv2.LINE_AA)

# 이미지를 창으로 출력
cv2.imshow("CIA", img)
# 아무 키 누르면 창 종료
cv2.waitKey(0)