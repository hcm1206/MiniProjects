# 이미지 카툰풍으로 변경

import cv2

# 원본 이미지 로드
img = cv2.imread('aha.jpg', cv2.IMREAD_COLOR)
# 이미지의 크기와 색 정보 추출
height, width, color = img.shape
# 이미지의 크기와 색 정보 출력
print(width, height, color)

# 너비 값을 400으로 하고 그에 맞는 비율의 높이 값을 설정하여 이미지 크기 조정
new_width = 400
new_height = int(height*new_width/width)
img_resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
# sigma_s(부드러운 정도), sigma_r(경계선 보존 정도) 매개변수를 설정하여 이미지를 카툰화
img_cartoon = cv2.stylization(img_resized, sigma_s=150, sigma_r=0.2)

# 카툰화된 이미지 창으로 출력
cv2.imshow('test', img_cartoon)
# 아무 키 누르면 종료
cv2.waitKey(0)