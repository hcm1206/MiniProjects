# 워터마크 위치 조정 기능 추가

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
# 사용자에게 워터마크 위치 입력받기
watermark_position = input("워터마크가 들어갈 위치 지정(LT:좌측 상단, LB:좌측 하단, C:정중앙, RT:우측 상단, RB:우측 하단>>)")

# LT 입력 시 생성한 워터마크 배경 이미지의 왼쪽 상단을 기준으로 정의한 수치(20)만큼 여백을 두어 워터마크 이미지 추가
if watermark_position == 'LT':
    watermark_background[MARGIN:watermark.shape[0]+MARGIN, MARGIN:watermark.shape[1]+MARGIN] = watermark
# LB 입력 시 생성한 워터마크 배경 이미지의 왼쪽 하단을 기준으로 정의한 수치(20)만큼 여백을 두어 워터마크 이미지 추가
elif watermark_position == 'LB':
    watermark_background[watermark_background.shape[0]-watermark.shape[0]-MARGIN:watermark_background.shape[0]-MARGIN, 
                         MARGIN:watermark.shape[1]+MARGIN] = watermark
# C 입력 시 생성한 워터마크 배경 이미지의 정중앙을 기준으로 워터마크 이미지 추가
elif watermark_position == 'C':
    watermark_background[
        int(watermark_background.shape[0]/2) - int(watermark.shape[0]/2) : int(watermark_background.shape[0]/2) - int(watermark.shape[0]/2) + watermark.shape[0],
        int(watermark_background.shape[1]/2) - int(watermark.shape[1]/2) : int(watermark_background.shape[1]/2) - int(watermark.shape[1]/2) + watermark.shape[1],
    ] = watermark
# RT 입력 시 생성한 워터마크 배경 이미지의 오른쪽 상단을 기준으로 워터마크 이미지 추가
elif watermark_position == 'RT':
    watermark_background[MARGIN:watermark.shape[0]+MARGIN,
                         watermark_background.shape[1]-watermark.shape[1]-MARGIN:watermark_background.shape[1]-MARGIN] = watermark
# RB 입력 시 생성한 워터마크 배경 이미지의 오른쪽 하단을 기준으로 워터마크 이미지 추가
elif watermark_position == 'RB':
    watermark_background[watermark_background.shape[0]-watermark.shape[0]-MARGIN:watermark_background.shape[0]-MARGIN,
                         watermark_background.shape[1]-watermark.shape[1]-MARGIN:watermark_background.shape[1]-MARGIN] = watermark

# 원본 이미지에 워터마크 배경 이미지 병합
result_img = cv2.addWeighted(img, 1.0, watermark_background, 1.0, 0)
# 병합된 이미지를 파일로 저장
cv2.imwrite('test_result.png', result_img)
# 병합된 이미지를 창으로 출력
cv2.imshow('result', result_img)
# 아무 키 입력 시 창을 닫고 프로그램 종료
cv2.waitKey(0)
cv2.destroyAllWindows()