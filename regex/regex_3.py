# 전화번호와 주민등록번호 정규식을 통해 추출하는 프로그램

import re

# 파일 로드 후 문자열 추출
with open('regex_test2.txt', 'r', encoding='UTF-8') as File:
    data = File.read()

# 원본 문자열 출력
print(data)

# 숫자 6개, -,  숫자 7개로 이루어진 주민등록번호 정규식 생성
p1 = re.compile(r'\d{6}[-]\d{7}')
# 원본 문자열에서 주민등록번호 정규식을 만족하는 부분 추출하여 리스트로 저장
rrn_list = re.findall(p1, data)
# 주민등록번호 리스트 내용 출력
print(rrn_list)

# 숫자 2개 또는 3개, -, 숫자 4개, -, 숫자 4개로 이루어진 전화번호 정규식 생성
p2 = re.compile(r'\d{2,3}[-]\d{4}[-]\d{4}')
# 원본 문자열에서 전화번호 정규식을 만족하는 부분 추출하여 리스트로 저장
phone_list = re.findall(p2, data)
# 전화번호 리스트 내용 추출
print(phone_list)