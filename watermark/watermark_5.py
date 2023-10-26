# 특정 디렉토리 내의 모든 이미지 파일에 워터마크 추가

import cv2
import numpy as np
import os
import imghdr

# 워터마크 여백 수치를 20으로 정의
MARGIN = 20

# 처리할 이미지가 포함된 디렉터리 경로 설정
path_dir = './src'
# 디렉터리 내 모든 파일 목록 저장
file_list = os.listdir(path_dir)

# result 디렉터리가 없으면 새로 생성
try:
    os.makedirs('result')
except FileExistsError:
    pass

# 사용자에게 워터마크 위치 입력받기
watermark_position = input("워터마크가 들어갈 위치 지정(LT:좌측 상단, LB:좌측 하단, C:정중앙, RT:우측 상단, RB:우측 하단)")

# 이미지 파일 목록 저장할 빈 리스트 생성
img_file_list = []
# 파일 전체 목록의 파일들을 확인하여 이미지 파일일 경우 파일 경로를 리스트에 추가
for file in file_list:
    if imghdr.what(path_dir + '\\' + file):
        img_file_list.append(file)

# 이미지 파일 목록에서 이미지 파일 별로 반복
for file in img_file_list:
    # 원본 이미지를 컬러로 로드
    img = cv2.imread(path_dir + '\\' + file, cv2.IMREAD_COLOR)
    # 워터마크로 사용할 이미지를 컬러로 로드
    watermark = cv2.imread('watermark.png', cv2.IMREAD_COLOR)
    # 원본 이미지와 동일한 크기의 검은색(0)으로 채워진 배경 이미지 생성
    watermark_background = np.zeros_like(img)

    # 입력받은 위치가 LT일 시 생성한 워터마크 배경 이미지의 왼쪽 상단을 기준으로 정의한 수치(20)만큼 여백을 두어 워터마크 이미지 추가
    if watermark_position == 'LT':
        watermark_background[MARGIN:watermark.shape[0]+MARGIN, MARGIN:watermark.shape[1]+MARGIN] = watermark
    # 입력받은 위치가 LB일 시 생성한 워터마크 배경 이미지의 왼쪽 하단을 기준으로 정의한 수치(20)만큼 여백을 두어 워터마크 이미지 추가
    elif watermark_position == 'LB':
        watermark_background[watermark_background.shape[0]-watermark.shape[0]-MARGIN:watermark_background.shape[0]-MARGIN,
                            MARGIN:watermark.shape[1]+MARGIN] = watermark
    # 입력받은 위치가 C일 시 생성한 워터마크 배경 이미지의 정중앙을 기준으로 워터마크 이미지 추가
    elif watermark_position == 'C':
        watermark_background[int(watermark_background.shape[0]/2)-int(watermark.shape[0]/2):int(watermark_background.shape[0]/2)-int(watermark.shape[0]/2)+watermark.shape[0],
                             int(watermark_background.shape[1]/2)-int(watermark.shape[1]/2):int(watermark_background.shape[1]/2)-int(watermark.shape[1]/2)+watermark.shape[1],
                             ] = watermark
    # 입력받은 위치가 RT일 시 생성한 워터마크 배경 이미지의 오른쪽 상단을 기준으로 정의한 수치(20)만큼 여백을 두어 워터마크 이미지 추가
    elif watermark_position == 'RT':
        watermark_background[MARGIN:watermark.shape[0]+MARGIN,
                             watermark_background.shape[1]-watermark.shape[1]-MARGIN:watermark_background.shape[1]-MARGIN] = watermark
    # 입력받은 위치가 RB일 시 생성한 워터마크 배경 이미지의 오른쪽 하단을 기준으로 정의한 수치(20)만큼 여백을 두어 워터마크 이미지 추가
    elif watermark_position == 'RB':
        watermark_background[watermark_background.shape[0]-watermark.shape[0]-MARGIN:watermark_background.shape[0]-MARGIN,
                             watermark_background.shape[1]-watermark.shape[1]-MARGIN:watermark_background.shape[1]-MARGIN] = watermark
    # 입력받은 위치가 유효하지 않을 시 오류 메시지 출력 및 중단
    else:
        print("워터마크 위치를 잘못 입력하셨습니다.")
        break
    
    # 원본 이미지에 워터마크 배경 이미지 병합
    result_img = cv2.addWeighted(img, 1.0, watermark_background, 1.0, 0)
    # result 디렉터리에 병합된 이미지를 파일로 저장
    cv2.imwrite('./result/result_' + file, result_img)