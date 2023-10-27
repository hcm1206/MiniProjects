# 말풍선에 글자 추가

import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

# 원본 이미지 로드
img = cv2.imread('aha.jpg', cv2.IMREAD_COLOR)
# 이미지의 크기와 색 정보 추출
height, width, color = img.shape
print(width, height, color)

# 너비 값을 400으로 하고 그에 맞는 비율의 높이 값을 설정하여 이미지 크기 조정
new_width = 400
new_height = int(height * new_width/width)
img_resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
# sigma_s(부드러운 정도), sigma_r(경계선 보존 정도) 매개변수를 설정하여 이미지를 카툰화
img_cartoon = cv2.stylization(img_resized, sigma_s=150, sigma_r=0.2)
# 카툰화된 이미지에서 말풍선으로 상용할 타원 추가
img_carton = cv2.ellipse(img_cartoon, (100, 380), (80, 60), 0, 0, 360, (80, 255, 255), -1)
# 카툰화된 이미지의 타입 출력(넘파이 배열)
print(type(img_cartoon))

# 카툰화된 이미지(넘파이 배열)을 PIL Image 객체로 변환
img_pillow = Image.fromarray(img_cartoon)
# Image 객체화된 카툰 이미지 타입 출력(PIL IMmage)
print(type(img_pillow))

# 폰트 경로 설정
fontpath = "fonts/gulim.ttc"
# 폰트 경로에 저장된 폰트 정보를 저장
font = ImageFont.truetype(fontpath, 24)
# 폰트 RGBA 색상 설정
b,g,r,a = 0,0,255,255
# 카툰 이미지에 글자를 넣기 위해 ImageDraw 객체 적용
draw = ImageDraw.Draw(img_pillow, 'RGBA')
# 카툰 이미지가 저장된 ImageDraw 객체에 설정한 폰트와 색상으로로 문자 입력
draw.text((75, 370), "아하!", font=font, fill=(b,g,r,a))
# PIL Image 객체의 카툰 이미지를 다시 넘파이 배열로 변환
img_numpy = np.array(img_pillow)
# 현재 카툰 이미지 타입 출력(넘파이 배열)
print(type(img_numpy))

# 최종 카툰 이미지 창으로 출력
cv2.imshow('test', img_numpy)
# 아무 키 누르면 종료
cv2.waitKey(0)