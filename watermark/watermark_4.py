# 특정 디렉터리의 이미지 파일 탐색

import os
import imghdr

# 탐색할 디렉터리 경로 설정
path_dir = './src'
# 해당 디렉터리의 모든 파일 목록 저장
file_list = os.listdir(path_dir)
# 파일 목록 출력
print(file_list)

# 이미지 파일 목록 저장할 빈 리스트 생성
img_file_list = []
# 파일 전체 목록의 파일들을 확인하여 이미지 파일일 경우 리스트에 추가
for file in file_list:
    if imghdr.what(path_dir + '\\' + file):
        img_file_list.append(file)

# 발견된 이미지 파일들이 저장된 리스트 출력
print(img_file_list)