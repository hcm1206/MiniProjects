# 워터마크에 여백 추가

import cv2
import numpy as np

# 워터마크 여백 수치를 20으로 정의
MARGIN = 20

# 원본 이미지를 컬러로 로드
img = cv2.imread('seoul1.jpg', cv2.IMREAD_COLOR)
# 워터마크로 사용할 이미지를 컬러로 로드
watermark = cv2.imread('watermark.png', cv2.IMREAD_COLOR)

# 원본 이미지와 동일한 크기의 검은색(0)으로 채워진 배경 이미지 생성
watermark_background = np.zeros_like(img)
# 생성한 워터마크 배경 이미지의 왼쪽 상단을 기준으로 정의한 수치(20)만큼 여백을 두어 워터마크 이미지 추가
watermark_background[MARGIN:watermark.shape[0]+MARGIN, MARGIN:watermark.shape[1]+MARGIN] = watermark
# 여백을 포함한 워터마크가 들어간 배경 이미지 출력
cv2.imshow('background', watermark_background)

# 원본 이미지에 워터마크 배경 이미지를 병합
result_img = cv2.addWeighted(img, 1.0, watermark_background, 1.0, 0)
# 병합된 이미지를 파일로 저장
cv2.imwrite('test_result.png', result_img)
# 병합된 이미지를 창으로 출력
cv2.imshow('result', result_img)
# 아무 키 입력 시 창을 닫고 프로그램 종료
cv2.waitKey(0)
cv2.destropyAllWindows()