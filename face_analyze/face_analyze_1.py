# DeepFace 라이브러리를 이용하여 얼굴 이미지 분석 내용 출력

from deepface import DeepFace

# 지정한 경로의 이미지에 나타난 얼굴을 분석하고 분석 내용을 출력
face_analysis = DeepFace.analyze(img_path = "test.jpg")
print(face_analysis)