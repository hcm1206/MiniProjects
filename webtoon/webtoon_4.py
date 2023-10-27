# 3컷의 카툰풍 이미지로 카툰 이미지 생성

import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

# 각 이미지 너비를 400으로 통일
new_width = 400
# 폰트 경로 설정
fontpath = "fonts/gulim.ttc"
# 폰트 경로에 저장된 폰트 정보를 저장
font = ImageFont.truetype(fontpath, 20)
# 폰트 RGBA 색상 설정
b,g,r,a = 0,0,0,255

# 각 컷의 대사를 리스트로 저장
script = ["꽥", "꽉", "까꿍"]
# 각 컷의 말풍선 위치를 리스트로 저장
ellipse_center = [(80, 150), (70, 50), (180, 170)]
# 각 컷의 텍스트 위치를 리스트로 저장
text_start = [(70, 140), (60, 40), (160, 160)]

# 각 컷을 통합할 넘파이 배열 생성
result_img = np.zeros((0, 400, 3), np.uint8)

# 1~3컷 이미지 반복
for i in range(1, 4):
    # 각 이미지 로드
    img = cv2.imread('cut' + str(i) + '.png', cv2.IMREAD_COLOR)
    # 이미지 크기와 색 추출
    height, width, color = img.shape
    # 너비 값(400)에 맞는 비율의 높이값 계산
    new_height = int(height * new_width/width)
    # 이미지 크기를 설정한 비율에 통일되도록 조정
    img_resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
    # 이미지 카툰화
    img_cartoon = cv2.stylization(img_resized, sigma_s=150, sigma_r=0.2)
    # 카툰화된 이미지에 리스트에서 설정한 위치대로 말풍선 추가
    img_cartoon = cv2.ellipse(img_cartoon, ellipse_center[i-1], (60, 40), 0, 0, 360, (230, 230, 230), -1)

    # 넘파이 배열 형태의 이미지를 PIL Image 객체 형태로 변환
    img_pillow = Image.fromarray(img_cartoon)
    # 카툰 이미지에 글자를 넣기 위해 ImageDraw 객체 적용
    draw = ImageDraw.Draw(img_pillow, 'RGBA')
    # 카툰 이미지가 저장된 ImageDraw 객체에 설정한 폰트 및 리스트에서 설정한 대로 대사 글자 추가
    draw.text(text_start[i-1], script[i-1], font=font, fill=(b,g,r,a))
    # PIL Image 객체를 넘파이 배열로 환원
    img_numpy = np.array(img_pillow)
    # 이미지를 넘파이 배열에 수직으로 통합
    result_img = cv2.vconcat([result_img, img_numpy])

# 최종 카툰 통합본 창으로 출력
cv2.imshow('test', result_img)
# 아무 키나 누르면 창 종료
cv2.waitKey(0)
# 최종 카툰 통합본 파일로 저장
cv2.imwrite("3cut_webtoon.jpg", result_img)